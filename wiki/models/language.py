# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import absolute_import

import hashlib

from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _, ugettext
from django.core.cache import cache
from django.db import models

from wiki.conf import settings

#lists all languages
@python_2_unicode_compatible
class Language(models.Model):
    #no spaces
    language =  models.CharField(primary_key=True, max_length=255, verbose_name=_('article language'), 
                             null=False, default='_', blank=False, help_text=_('Category by programming language'))
    language_displayname =  models.CharField(max_length=512, verbose_name=_('article language display name'), 
                             null=False, default='_', blank=False, help_text=_('Category by programming language'))
    language_description =  models.CharField(max_length=1024, verbose_name=_('article language description'), 
                             null=False, default='_', blank=False, help_text=_('Category by programming language'))

    class Meta:
        managed = True
        app_label = settings.APP_LABEL

    def __str__(self):
        obj_name = _('Language %s displayed as %s' % (self.language, self.language_displayname))
        return str(obj_name)

    @classmethod
    def get_all_languages(cls):
        key = 'languagelist'
        all_langs = cache.get(key)
        if all_langs is not None:
            # cache hit
            return all_langs
        # cache miss
        query = cls.objects.all()
        all_langs = [(l.language, l.language_displayname, l.language_description) for l in query]
        cache.set(key, all_langs)
        return all_langs

    @classmethod
    def get_displayname(cls, language):
        all_langs = cls.get_all_languages()
        try:
            res = [l[1] for l in all_langs if l[0]==language]
            return res[0]
        except IndexError:
            return " "

    @classmethod
    def get_description(cls, language):
        all_langs = cls.get_all_languages()
        try:
            res = [l[2] for l in all_langs if l[0]==language]
            return res[0]
        except IndexError:
            return " "

    @classmethod
    def lang_to_rgb_arr(cls, language):
        """
        Produce rgb values for css.
        css font and background colors take a 24 bit rgb value.
        """
        key = 'languagergbarray_%s' % language
        rgb = cache.get(key)
        if rgb is not None:
            return rgb
        # only need 24 bits out of 160
        d = hashlib.sha1(language).hexdigest()[0:6]
        b1, b2, b3 = int(d[:2], 16), int(d[2:4], 16), int(d[4:], 16)
        # b1 manipulated and b2, b3 swapped so that C don't have a shitty color ;)
        b1 = b2 * b3 % 256
        cache.set(key, [b1, b3, b2])
        return [b1, b3, b2]

    @classmethod
    def lang_to_rgb(cls, language):
        r, g, b = cls.lang_to_rgb_arr(language)
        return "rgb(%s, %s, %s)" % (str(r), str(g), str(b))

    @classmethod
    def lang_to_fontcolor_rgb(cls, language):
        r,g,b = cls.lang_to_rgb_arr(language);
        luminance = 0.2126*r + 0.7152*g + 0.0722*b
        return "white" if luminance < 128 else "black"

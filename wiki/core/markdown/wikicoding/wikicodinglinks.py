'''
WikicodingLinks Extension for Python-Markdown
=============================================

Converts [[WikicodingLinks]] to relative links.

Adpater from WikiLinks Extension for Python-Markdown.

See <https://pythonhosted.org/Markdown/extensions/wikilinks.html>
for documentation.

Original code Copyright [Waylan Limberg](http://achinghead.com/).

All changes Copyright Arjun Sreedharan <arjun024@gmail.com>

License: [BSD](http://www.opensource.org/licenses/bsd-license.php)

---------------------------------------------
examples:

[[Formatting]]
-> <a class="wikicodinglink" href="/wiki/Formatting/" target="_blank">Formatting</a>

[[c:Merge sort]]
-> <a class="wikicodinglink" href="/wiki/c/Merge_sort/" target="_blank">Merge sort (c)</a>

[[c:Merge sort|best sort ever]]
-> <a class="wikicodinglink" href="/wiki/c/Merge_sort/" target="_blank">best sort ever</a>

'''


from __future__ import absolute_import
from __future__ import unicode_literals
from markdown import Extension
from markdown.inlinepatterns import Pattern
from markdown.util import etree
import re


def build_url(lang, label, base, end):
    """ Build a url from the label, a base, and an end. """
    clean_label = re.sub(r'([ ]+_)|(_[ ]+)|([ ]+)', '_', label)
    lang = lang + "/" if lang != "_" else ""
    url = '%s%s%s%s' % (base, lang, clean_label, end)
    # no trailing slash when pointing to sections
    if "#" in url: return url.rstrip('/')
    return url


class WikiLinkExtension(Extension):
    def __init__(self, *args, **kwargs):
        self.config = {
            'base_url': ['/wiki/', 'String to append to beginning or URL.'],
            'end_url': ['/', 'String to append to end of URL.'],
            'html_class': ['wikicodinglink', 'CSS hook. Leave blank for none.'],
            'build_url': [build_url, 'Callable formats URL from label.'],
        }

        super(WikiLinkExtension, self).__init__(*args, **kwargs)

    def extendMarkdown(self, md, md_globals):
        self.md = md
        # append to end of inline patterns
        WIKILINK_RE = r'\[\[([:#|\w0-9_ \.\+\)\(-]+)\]\]'
        wikilinkPattern = WikiLinks(WIKILINK_RE, self.getConfigs())
        wikilinkPattern.md = md
        md.inlinePatterns.add('wikicodinglink', wikilinkPattern, "<not_strong")


class WikiLinks(Pattern):
    def __init__(self, pattern, config):
        super(WikiLinks, self).__init__(pattern)
        self.config = config

    @staticmethod
    def build_category_url(category):
        return "/wiki/Category:%s" % category

    @staticmethod
    def build_user_url(username):
        return "/%s" % username

    def handleMatch(self, m):
        # The pattern here is u'^(.*?)\\[\\[([:\\w0-9_ -]+)\\]\\](.*?)$'
        # see https://pythonhosted.org/Markdown/extensions/api.html#inlinepatterns
        if m.group(2).strip():
            base_url, end_url, html_class = self._getMeta()
            raw_label = m.group(2).strip()
            explicit_label = False
            raw_lst = raw_label.split('|')
            if len(raw_lst) > 1:
                explicit_label = True
                raw_label, final_label = raw_lst[0], raw_lst[1]
            raw_lst = raw_label.split(':')
            if len(raw_lst) > 1:
                lang, label = raw_lst[0], raw_lst[1]
            else:
                lang, label = "_", raw_lst[0]
            lang = "_" if lang == "" else lang
            if lang.lower() == "user":
                url = self.build_user_url(label)
            elif lang.lower() == "category":
                url = self.build_category_url(label)
            else:
                url = self.config['build_url'](lang, label, base_url, end_url)
            if explicit_label is False:
                final_label = "%s%s%s%s" % (label, " (", raw_lst[0], ")") if lang != "_" else label
            final_label = label if lang.lower() == "user" else final_label
            a = etree.Element('a')
            a.text = final_label
            if lang.lower() == "user":
                a.set('style', 'color: #4A00FF')
            a.set('href', url)
            if html_class:
                a.set('class', html_class)
        else:
            a = ''
        return a

    def _getMeta(self):
        """ Return meta data or config data. """
        base_url = self.config['base_url']
        end_url = self.config['end_url']
        html_class = self.config['html_class']
        if hasattr(self.md, 'Meta'):
            if 'wiki_base_url' in self.md.Meta:
                base_url = self.md.Meta['wiki_base_url'][0]
            if 'wiki_end_url' in self.md.Meta:
                end_url = self.md.Meta['wiki_end_url'][0]
            if 'wiki_html_class' in self.md.Meta:
                html_class = self.md.Meta['wiki_html_class'][0]
        return base_url, end_url, html_class


def makeExtension(*args, **kwargs):
    return WikiLinkExtension(*args, **kwargs)

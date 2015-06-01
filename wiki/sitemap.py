import datetime
from wiki import models
from django.contrib import sitemaps
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


class WikiSitemap(sitemaps.Sitemap):

    def items(self):
        return models.urlpath.URLPath.objects.all()

    def changefreq(self, obj):
        return "daily"

    def priority(self, obj):
        if obj.language == '_' and obj.path.strip('/') == "":
            return 0.0
        if obj.language == '_' and obj.path.strip('/') == "Main_Page":
            return 1.0
        return 0.5

    def lastmod(self, obj):
        return datetime.datetime.now()

    def location(self, obj):
        language = obj.language
        path = obj.path
        if language == '_':
            return "/wiki/%s" % path
        return reverse("wiki:get", kwargs={'language': language, 'path': path})

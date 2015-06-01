# -*- coding: utf-8 -*-
"""
Handle category page
"""

from __future__ import unicode_literals
from __future__ import absolute_import
from django.http import HttpResponse
from django.utils.translation import ugettext as _
from django.views.generic.list import ListView

from wiki import models

class CategoryPage(ListView):
    template_name="wiki/category_page.html"
    allow_empty = True
    context_object_name = 'urlpaths'
    paginate_by = 20

    def get_queryset(self):
        self.category = self.kwargs["category"].strip("/")
        self.category = "_" if self.category == "text_article" else self.category
        return models.URLPath.objects.filter(language=self.category).order_by('slug')

    def get_context_data(self, **kwargs):
        context = super(CategoryPage, self).get_context_data(**kwargs)
        context['category'] = self.category
        return context

    def dispatch(self, request, category, *args, **kwargs):
        return super(CategoryPage, self).dispatch(request, category, *args, **kwargs)

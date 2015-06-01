# -*- coding: utf-8 -*-
"""
Handle recent revisions page
"""

from __future__ import unicode_literals
from __future__ import absolute_import
from django.http import HttpResponse
from django.utils.translation import ugettext as _
from django.views.generic.list import ListView

from wiki import models

class RecentPage(ListView):
    template_name="wiki/recent_page.html"
    allow_empty = True
    context_object_name = 'revisions'
    paginate_by = 50

    def get_queryset(self):
        return models.ArticleRevision.objects.all().order_by('-created')

    def get_context_data(self, **kwargs):
        context = super(RecentPage, self).get_context_data(**kwargs)
        return context

    def dispatch(self, request, *args, **kwargs):
        return super(RecentPage, self).dispatch(request, *args, **kwargs)

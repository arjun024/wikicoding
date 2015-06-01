# -*- coding: utf-8 -*-
"""
Handle user contribution page
"""

from __future__ import unicode_literals
from __future__ import absolute_import
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from django.views.generic.list import ListView

from wiki import models

from wiki.core.compat import get_user_model
User = get_user_model()

import socket

class UserPage(ListView):
    template_name="wiki/user_page.html"
    allow_empty = True
    context_object_name = 'revisions'
    paginate_by = 20

    def get_queryset(self):
        username = self.kwargs["username"].strip("/")
        try:
            socket.inet_aton(username)
            # is an ip address
            self.ip_address = username
            return models.ArticleRevision.objects.all().filter(ip_address=self.ip_address).order_by('-created')
        except socket.error:
            # probably username
            self.userpage_user = User.objects.filter(username__iexact=username)[0]
            return models.ArticleRevision.objects.all().filter(user_id=self.userpage_user.pk).order_by('-created')

    def get_context_data(self, **kwargs):
        context = super(UserPage, self).get_context_data(**kwargs)
        if hasattr(self, 'ip_address'):
            context['userpage_user'] = {'username': self.ip_address},
            context['usertype'] = 'ip_address'
        else:
            context['userpage_user'] = self.userpage_user
            context['usertype'] = 'username'
        return context

    def dispatch(self, request, username, *args, **kwargs):
        return super(UserPage, self).dispatch(request, username, *args, **kwargs)

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django_mysql.models import JSONField

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User


class Post(models.Model):
    class Meta:
        verbose_name = _('VK wall post')
        verbose_name_plural = _('VK wall posts')

    user = models.ForeignKey(User, verbose_name=_('user'), related_name='posts', blank=False, null=False,
            on_delete=models.CASCADE)
    details = JSONField(verbose_name=_('details'), blank=False, null=False)
    extracted = models.DateTimeField(verbose_name=_('Extraction datetime'), auto_now_add=True, blank=False, null=False)

    # denormalized fields copying data from details for search purposes
    # just for demonstration purpose
    vk_id = models.IntegerField(verbose_name=_('id for owner'), blank=False, null=False)
    vk_owner_id = models.IntegerField(verbose_name=_('owner id'), blank=False, null=False)

    def __unicode__(self):
        return 'Post #{} by {} (extracted {})'.format(
            self.vk_id, self.vk_owner_id, self.extracted.isoformat()
        )

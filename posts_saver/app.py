from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class PostsSaverAppConfig(AppConfig):
    name = 'posts_saver'
    verbose_name = _('Posts saver')

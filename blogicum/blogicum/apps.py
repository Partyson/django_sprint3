from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class BlogicumConfig(AppConfig):
    name = 'blogicum'
    verbose_name = _("Блог")

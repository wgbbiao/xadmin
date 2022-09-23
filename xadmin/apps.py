from django.apps import AppConfig
from django.core import checks
from django.utils.translation import gettext as _
import xadmin


class XAdminConfig(AppConfig):
    """Simple AppConfig which does not do automatic discovery."""
    default_auto_field = 'django.db.models.BigAutoField'

    name = 'xadmin'
    verbose_name = "Administration"

    def ready(self):
        self.module.autodiscover()
        setattr(xadmin, 'site', xadmin.site)

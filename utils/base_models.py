from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))
    modified_at = models.DateTimeField(auto_now=True, verbose_name=_('modified at'))

    class Meta:
        abstract = True

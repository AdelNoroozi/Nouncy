from django.core.exceptions import ValidationError
from django.db import models

from accounts.models import BaseUser, ContentManager
from utils.base_models import BaseModel
from django.utils.translation import gettext_lazy as _


class Announcement(BaseModel):
    STATUSES = (('WFP', _('waiting for publish')),
                ('WFR', _('waiting for review')),
                ('RWFP', _('reviewed and waiting for publish')),
                ('P', _('published')),
                ('R', _('rejected')))

    title = models.CharField(max_length=50, verbose_name=_('title'))
    content = models.TextField(verbose_name=_('content'))
    creator = models.ForeignKey(BaseUser, on_delete=models.RESTRICT, related_name='announcements',
                                verbose_name=_('creator'))
    assigned_reviewer = models.ForeignKey(ContentManager, on_delete=models.RESTRICT, blank=True, null=True,
                                          related_name='announcements', verbose_name=_('assigned_reviewer'))
    status = models.CharField(max_length=30, choices=STATUSES, default='WFP', verbose_name=_('status'))

    @staticmethod
    def validate_creator_role(creator: BaseUser):
        if creator.role == 'CM' or creator.role == 'UD':
            raise ValidationError("Announcements creators must be clients or publishers")

    def clean(self):
        super().clean()
        self.validate_creator_role(self.creator)

    def __str__(self):
        return f'{self.title} - {self.creator.username}'

    class Meta:
        verbose_name = _('Announcement')
        verbose_name_plural = _('Announcements')

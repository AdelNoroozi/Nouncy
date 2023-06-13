from django.contrib.auth.hashers import make_password
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from utils.base_models import BaseModel


class UserManager(models.Manager):
    def get_by_natural_key(self, username):
        return self.get(username=username)

    def create_user(self, username, password):
        if not username:
            raise ValueError("username is required")
        if not password:
            raise ValueError("password is required")
        user_obj = self.model(
            username=username,
        )
        user_obj.password = make_password(password)
        user_obj.role = 'UD'
        user_obj.save(using=self._db)
        return user_obj

    def create_client(self, username, password):
        client = self.create_user(username, password)
        client.role = 'CLN'
        client.save(using=self._db)
        return client

    def create_content_manager(self, username, password):
        client = self.create_user(username, password)
        client.role = 'CM'
        client.save(using=self._db)
        return client

    def create_publisher(self, username, password):
        client = self.create_user(username, password)
        client.role = 'PUB'
        client.save(using=self._db)
        return client

    def create_superuser(self, username, password):
        client = self.create_user(username, password)
        client.role = 'SU'
        client.is_staff = True
        client.save(using=self._db)
        return client


class BaseUser(BaseModel):
    ROLES = (('SU', _('superuser')),
             ('PUB', _('publisher')),
             ('CM', _('content manager')),
             ('CLN', _('client')),
             ('UD', _('undefined')))

    username_validator = UnicodeUsernameValidator()

    username = models.CharField(max_length=50, unique=True, validators=[UnicodeUsernameValidator],
                                verbose_name=_("username"))
    password = models.CharField(max_length=128, verbose_name=_('password'))
    role = models.CharField(max_length=10, choices=ROLES, verbose_name=_('role'))
    is_active = models.BooleanField(default=True, verbose_name=_('is active'))
    is_staff = models.BooleanField(default=False, verbose_name=_('is staff'))

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = UserManager()

    @property
    def is_anonymous(self):
        return False

    @property
    def is_authenticated(self):
        return True

    def has_perm(self, perm, obj=None):
        if self.is_active and self.is_staff:
            return True

    def has_module_perms(self, app_label):
        return self.has_perm(self)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = _('Base User')
        verbose_name_plural = _('Base Users')

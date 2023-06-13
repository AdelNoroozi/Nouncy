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
        Client.objects.create(base_user=client)
        return client

    def create_content_manager(self, username, password):
        content_manager = self.create_user(username, password)
        content_manager.role = 'CM'
        content_manager.save(using=self._db)
        ContentManager.objects.create(base_user=content_manager)
        return content_manager

    def create_publisher(self, username, password):
        publisher = self.create_user(username, password)
        publisher.role = 'PUB'
        publisher.save(using=self._db)
        Publisher.objects.create(base_user=publisher)
        return publisher

    def create_superuser(self, username, password):
        superuser = self.create_user(username, password)
        superuser.role = 'SU'
        superuser.is_staff = True
        superuser.save(using=self._db)
        return superuser


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
        return f'{self.username} - {self.role}'

    class Meta:
        verbose_name = _('Base User')
        verbose_name_plural = _('Base Users')


class Client(models.Model):
    base_user = models.OneToOneField(BaseUser, on_delete=models.CASCADE, related_name='client',
                                     verbose_name=_('base user'))

    # some extra fields that are specific to the client

    def __str__(self):
        return self.base_user.username

    class Meta:
        verbose_name = _('Client')
        verbose_name_plural = _('Clients')


class Publisher(models.Model):
    base_user = models.OneToOneField(BaseUser, on_delete=models.CASCADE, related_name='publisher',
                                     verbose_name=_('base user'))

    # some extra fields that are specific to the publisher

    def __str__(self):
        return self.base_user.username

    class Meta:
        verbose_name = _('Publisher')
        verbose_name_plural = _('Publishers')


class ContentManager(models.Model):
    base_user = models.OneToOneField(BaseUser, on_delete=models.CASCADE, related_name='content_manager',
                                     verbose_name=_('base user'))

    # some extra fields that are specific to the content manager

    def __str__(self):
        return self.base_user.username

    class Meta:
        verbose_name = _('Content Manager')
        verbose_name_plural = _('Content Managers')

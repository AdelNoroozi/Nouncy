from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password

from .models import BaseUser


class AuthBackend(BaseBackend):
    def authenticate(self, request, **kwargs):
        username = kwargs.get('username')
        password = kwargs.get('password')

        if username is None or password is None:
            return None

        try:
            user = BaseUser.objects.get(username=username)
            if check_password(password, user.password):
                return user
        except BaseUser.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return BaseUser.objects.get(id=user_id)
        except BaseUser.DoesNotExist:
            return None

from rest_framework.generics import CreateAPIView
from accounts.models import BaseUser
from accounts.serializers import RegisterClientSerializer


class RegisterClientView(CreateAPIView):
    queryset = BaseUser.objects.all()
    serializer_class = RegisterClientSerializer

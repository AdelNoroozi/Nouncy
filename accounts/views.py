from rest_framework.generics import CreateAPIView
from accounts.models import BaseUser
from accounts.serializers import RegisterClientSerializer, AddPublisherSerializer


class RegisterClientView(CreateAPIView):
    queryset = BaseUser.objects.all()
    serializer_class = RegisterClientSerializer


class AbstractAddActorView(CreateAPIView):
    queryset = BaseUser.objects.all()


class AddPublisherView(AbstractAddActorView):
    serializer_class = AddPublisherSerializer


class AddContentManagerSerializer(AbstractAddActorView):
    serializer_class = AddPublisherSerializer

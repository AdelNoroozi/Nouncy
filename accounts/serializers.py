from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from accounts.models import BaseUser


class RegisterClientSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = BaseUser
        fields = ('username', 'password')

    def validate(self, attrs):
        password = attrs.get('password')
        if password:
            validate_password(password)
        return attrs

    def create(self, validated_data):
        client = self.Meta.model.objects.create_client(**self.validated_data)
        return client


class AbstractAddActorSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = BaseUser
        fields = ('username', 'password')

    def validate(self, attrs):
        password = attrs.get('password')
        if password:
            validate_password(password)
        return attrs


# Publisher serializers
class AddPublisherSerializer(AbstractAddActorSerializer):

    def create(self, validated_data):
        publisher = self.Meta.model.objects.create_publisher(**self.validated_data)
        return publisher


class AddContentManagerSerializer(AbstractAddActorSerializer):

    def create(self, validated_data):
        content_manager = self.Meta.model.objects.create_content_manager(**self.validated_data)
        return content_manager

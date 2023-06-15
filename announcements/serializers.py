from rest_framework import serializers

from accounts.serializers import BaseUserMiniSerializer
from announcements.models import Announcement


class AnnouncementSerializer(serializers.ModelSerializer):
    creator = BaseUserMiniSerializer(many=False)

    class Meta:
        model = Announcement
        fields = '__all__'


class AnnouncementMiniSerializer(serializers.ModelSerializer):
    creator = BaseUserMiniSerializer(many=False)

    class Meta:
        model = Announcement
        fields = ('id', 'title', 'creator', 'status')


class SaveAnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = '__all__'
        read_only_fields = ('id', 'creator', 'assigned_reviewer', 'status', 'created_at', 'modified_at')

    def validate(self, attrs):
        creator = self.context['user']
        if creator.role == 'CM':
            raise serializers.ValidationError("Announcements creators must be clients or publishers")
        return attrs

    def create(self, validated_data):
        user = self.context['user']
        status = None
        if user.role == 'PUB' or user.role == 'SU':
            status = 'P'
        additional_data = {
            'creator': user
        }
        if status:
            additional_data['status'] = status
        announcement = self.Meta.model.objects.create(**validated_data, **additional_data)
        return announcement

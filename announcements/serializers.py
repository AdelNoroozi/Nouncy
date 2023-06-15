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

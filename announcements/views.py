from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.generics import get_object_or_404

from accounts.models import ContentManager
from announcements.models import Announcement
from announcements.serializers import AnnouncementSerializer, AnnouncementMiniSerializer


class AnnouncementViewSet(viewsets.ModelViewSet):

    def get_serializer_class(self):
        if self.action == 'list':
            return AnnouncementMiniSerializer
        if self.action == 'retrieve':
            return AnnouncementSerializer

    def get_queryset(self):
        if self.request.user.is_anonymous:
            return Announcement.objects.none()
        user = self.request.user
        if user.role == 'PUB' or user.role == 'SU':
            return Announcement.objects.all()
        if user.role == 'CM':
            reviewer = get_object_or_404(ContentManager, base_user=user)
            return Announcement.objects.filter(assigned_reviewer=reviewer)
        if user.role == 'CLN':
            return Announcement.objects.filter(creator=user)
        return Announcement.objects.none()

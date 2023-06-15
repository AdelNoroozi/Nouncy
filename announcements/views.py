from rest_framework import viewsets
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.generics import get_object_or_404
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from accounts.models import ContentManager
from accounts.permissions import AnnouncementPermission
from announcements.filters import AnnouncementFilter
from announcements.models import Announcement
from announcements.serializers import AnnouncementSerializer, AnnouncementMiniSerializer, SaveAnnouncementSerializer


class AnnouncementViewSet(viewsets.ModelViewSet):
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    permission_classes = (AnnouncementPermission, )
    search_fields = ['title', 'content']
    ordering_fields = ['title', 'created_at', 'modified_at']
    filterset_class = AnnouncementFilter

    def get_serializer_class(self):
        if self.action == 'list':
            return AnnouncementMiniSerializer
        if self.action == 'retrieve':
            return AnnouncementSerializer
        if self.action == 'create' or self.action == 'update' or self.action == 'partial_update':
            return SaveAnnouncementSerializer

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

    def get_serializer_context(self):
        if self.request.user.is_anonymous:
            raise AuthenticationFailed
        return {'user': self.request.user}

    def perform_update(self, serializer: SaveAnnouncementSerializer):
        announcement = serializer.instance
        if not self.request.user.role == 'PUB':
            announcement.status = 'WFP'
        else:
            announcement.status = announcement.status
        announcement.save()
        serializer.save()


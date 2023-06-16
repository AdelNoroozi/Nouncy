from rest_framework.permissions import BasePermission, SAFE_METHODS

from announcements.models import Announcement


class AnnouncementPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return False
        user = request.user
        if user.role == 'SU':
            return True
        if request.method in SAFE_METHODS:
            return True
        else:
            return user.role != 'CM'

    def has_object_permission(self, request, view, obj: Announcement):
        if not request.method in SAFE_METHODS:
            if obj.creator.role == 'PUB' or obj.creator.role == 'SU':
                if obj.creator == request.user:
                    return True
                else:
                    return False
        return True


class IsPublisher(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return False
        return request.user.role == 'PUB' or request.user.role == 'SU'


class IsPublisherOrContentManager(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return False
        return request.user.role == 'PUB' or request.user.role == 'CM' or request.user.role == 'SU'


class NotAuthenticated(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_anonymous


class IsSuperuser(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return False
        return request.user.role == 'SU'


class IsAuthenticated(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated

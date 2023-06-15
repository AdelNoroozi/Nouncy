from rest_framework.permissions import BasePermission, SAFE_METHODS


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


class IsPublisher(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return False
        return request.user.role == 'PUB' or request.user.role == 'SU'


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

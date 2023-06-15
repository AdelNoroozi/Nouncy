from django_filters import FilterSet
from .models import Announcement


class AnnouncementFilter(FilterSet):
    class Meta:
        model = Announcement
        fields = {
            'status': ['exact'],
            'creator': ['exact'],
            'creator__role': ['exact'],
            'assigned_reviewer': ['exact'],
            'created_at': ['gt', 'lt'],
            'modified_at': ['gt', 'lt']
        }

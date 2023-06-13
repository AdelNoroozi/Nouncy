from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from accounts.views import RegisterClientView, GetUserInfoView

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path("register/", RegisterClientView.as_view(), name='register'),
    path("add-publisher/", RegisterClientView.as_view(), name='add_publisher'),
    path("add-content-manager/", RegisterClientView.as_view(), name='add_content_manager'),
    path("whoami/", GetUserInfoView.as_view(), name='get_user_info'),
]

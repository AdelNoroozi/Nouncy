from django.urls import path

from accounts.views import RegisterClientView

urlpatterns = [
    path("register/", RegisterClientView.as_view(), name='register')
]

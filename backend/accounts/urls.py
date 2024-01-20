from django.urls import path
from .views import UserInfoView

urlpatterns = [
    path("", UserInfoView.as_view()),
]
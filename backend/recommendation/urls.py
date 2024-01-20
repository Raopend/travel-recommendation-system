from django.urls import path

from .views import RecommendTours

urlpatterns = [
    path("", RecommendTours.as_view()),
]

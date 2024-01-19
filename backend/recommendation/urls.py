from django.urls import path

from .views import recommend_tours

urlpatterns = [
    path('', recommend_tours, name='recommend_tours'),
]

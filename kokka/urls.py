from django.urls import path

from .views import home

urlpatterns = [
    path('arip/', home, name='home'),
]
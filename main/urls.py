
from django.urls import path
from .views import babyshark

urlpatterns = [
    path('babyshark', babyshark)
]

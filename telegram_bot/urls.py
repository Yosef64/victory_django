from django.urls import path
from . import views

urlpatterns = [
    path('api/index', views.webhook, name='telegram-webhook'),
]

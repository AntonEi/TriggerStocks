from . import views
from django.urls import path

urlpatterns = [
    path('', views.share_trigger, name='sharetrigger'),
]
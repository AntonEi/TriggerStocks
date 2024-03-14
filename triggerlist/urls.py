from . import views
from django.urls import path

urlpatterns = [
    path('', views.TriggerList.as_view(), name='home'),
]
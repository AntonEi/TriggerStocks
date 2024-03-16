from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.TriggerList.as_view(), name='home'),
    path('search', views.TriggerSearch.as_view(), name='search'),
    path("accounts/", include("allauth.urls")),
]
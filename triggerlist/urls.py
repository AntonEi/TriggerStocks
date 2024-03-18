from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.TriggerList.as_view(), name='home'),
    path('<slug:slug>/', views.trigger_detail, name='trigger_detail'),
    path('<slug:slug>/edit_comment/<int:comment_id>/',
         views.comment_edit, name='comment_edit'),
]
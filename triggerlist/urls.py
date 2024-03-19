from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.TriggerList.as_view(), name='home'),
    path('favourites/', views.favourite_list, name='favourite_list'),
    path('fav/<trigger_id>/', views.favourite_add, name='favourite_add'),
    path('<slug:slug>/', views.trigger_detail, name='trigger_detail'),
    path('<slug:slug>/edit_comment/<int:comment_id>/', views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>/', views.comment_delete, name='comment_delete'),
    # Remove the inclusion of sharetrigger.urls from here
]

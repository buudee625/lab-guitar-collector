from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('guitars/', views.guitar_index, name='index'),
    path('guitars/<int:gtr_id>/', views.guitar_detail, name='detail'),
    path('guitars/create/', views.GtrCreate.as_view(), name='gtr_create'),
    path('guitars/<int:pk>/update/', views.GtrUpdate.as_view(), name='gtr_update'),
    path('guitars/<int:pk>/delete/', views.GtrDelete.as_view(), name='gtr_delete'),
]
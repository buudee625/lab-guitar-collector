from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    # Guitars
    path('guitars/', views.guitar_index, name='index'),
    path('guitars/<int:gtr_id>/', views.guitar_detail, name='detail'),
    path('guitars/create/', views.GtrCreate.as_view(), name='gtr_create'),
    path('guitars/<int:pk>/update/', views.GtrUpdate.as_view(), name='gtr_update'),
    path('guitars/<int:pk>/delete/', views.GtrDelete.as_view(), name='gtr_delete'),
    path('guitars/<int:gtr_id>/add_review/', views.add_review, name='add_review'),
    # Players
    path('players/', views.PlayerIndex.as_view(), name='player_index'),
    path('players/<int:pk>/', views.PlayerDetail.as_view(), name='player_detail'),
    path('players/create/', views.PlayerCreate.as_view(), name='player_create'),
    path('players/<int:pk>/update/', views.PlayerUpdate.as_view(), name='player_update'),
    path('players/<int:pk>/delete/', views.PlayerDelete.as_view(), name='player_delete'),
]
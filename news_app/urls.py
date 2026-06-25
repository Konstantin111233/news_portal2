from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

app_name = 'news_app'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('news/<int:news_id>/', views.news_detail_view, name='news_detail'),  # <-- ЭТОТ МАРШРУТ
    path('news/add/', views.news_create_view, name='news_create'),
    path('news/<int:news_id>/edit/', views.news_edit_view, name='news_edit'),
    path('news/<int:news_id>/delete/', views.news_delete_view, name='news_delete'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', LogoutView.as_view(next_page='news_app:home'), name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('profile/delete/', views.profile_delete_view, name='profile_delete'),
]
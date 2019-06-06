from django.urls import path

from . import views


app_name = 'users'

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.CustomLoginView.as_view(template_name='users_app/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('edit_profile/delete_user/', views.delete_user, name='delete_user'),
    path('edit_profile/confirm_delete_user/', views.confirm_delete_user, name='confirm_delete_user'),
    path('vk_view/', views.vk_view, name='vk_view'),
]

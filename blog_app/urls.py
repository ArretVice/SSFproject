from django.urls import path, include
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.PostList.as_view(), name='all_posts'),
    path('<int:pk>/details/', views.PostDetails.as_view(), name='post_details'),
    path('create/', views.CreatePost.as_view(), name='create_post'),
    path('<int:pk>/edit/', views.EditPost.as_view(), name='edit_post'),
    path('<int:pk>/delete/', views.DeletePost.as_view(), name='delete_post'),
    path('user/<str:username>', views.PostsByUser.as_view(), name='posts_by_user'),
]
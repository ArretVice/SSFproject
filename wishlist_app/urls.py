from django.urls import path
from . import views


app_name = 'wishlist'

urlpatterns = [
    path('', views.all_wishlists_view, name='wishlists'),
    path('<int:user_id>/edit/<int:item_id>/', views.edit_item, name='edit_item'),
    path('<int:user_id>/edit/', views.edit_wishlist, name='edit_wishlist'),
    path('<int:user_id>/add/', views.add_item, name='add_item'),
    path('<int:user_id>/delete/<int:item_id>/', views.delete_item, name='delete_item'),
    path('<int:user_id>/confirm_delete/<int:item_id>/', views.confirm_delete_item, name='confirm_delete_item'),
]

from django.urls import path
from . import views
from post.views import all_Post

urlpatterns = [
    path('dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('delete-post/<int:post_id>/', views.admin_delete_post, name='admin_delete_post'),
    path('block-user/<int:user_id>/', views.admin_block_user, name='admin_block_user'),
    path('delete-user/<int:user_id>/', views.admin_delete_user, name='admin_delete_user'),
]

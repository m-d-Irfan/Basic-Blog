
from django.contrib import admin
from django.urls import path , include
from post.views import all_Post,post_details, create_post, update_post, delete_post


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', all_Post, name="all_Post"),
    path('post/<int:id>', post_details, name="post_details"),
    path('addpost/', create_post, name="add_post"),
    path('updatepost/<int:id>', update_post, name="update_post"),
    path('deletepost/<int:id>', delete_post, name="delete_post"),
    path('mypost/<int:uid>',all_Post , name="my_post"),
    path('users/',include("users.urls")),
    path('',include("catagory.urls"))
]

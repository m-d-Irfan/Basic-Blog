from django.urls import path , include
from .views import catagory_list,createview,updateView,deleteView
from post.views import all_Post


urlpatterns = [
    path('catagory/',catagory_list.as_view(),name='cata_list'),
    path('catagory/add/', createview.as_view(), name="cata_add"),
    path('catagory/update/<int:pk>', updateView.as_view(), name="cata_update"),
    path('catagory/delete/<int:pk>', deleteView.as_view(), name="cata_delete"),
    path('catagory/post/<int:cid>',all_Post,name='cata_post')
    
]

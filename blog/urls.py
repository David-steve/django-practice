from django.urls import path
from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post_detail/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit', views.post_edit, name='post_edit'),
    path('golden_point/', views.golden_point, name='golden_point'),
    path('v2ray_nodes/', views.v2ray_nodes, name='v2ray_nodes'),
    path('clash_nodes/', views.clash_nodes, name='v2ray_nodes'),
]
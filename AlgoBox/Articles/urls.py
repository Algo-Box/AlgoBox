from . import views
from django.urls import path


urlpatterns = [
    path('', views.PostList, name='home'),
    path('post/<slug:slug>/', views.PostDetail, name='post_detail'),
    path('create_article/', views.create_article, name='create_article'),
]
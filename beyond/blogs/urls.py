"""auth URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from . import views
from django.urls import path, include
from .views import *

app_name = 'blog'

urlpatterns = [
    path('create/', views.PostCreate.as_view(),name='blog_create'),
    path('', views.PostList.as_view(),name='blog_list'),    
    path('detail/<int:id>/', views.PostDetail.as_view(), name='post_detail'),
    path('delete/<int:id>/', views.PostDelete.as_view(), name='post_delete'),
    path('edit/<int:id>/', views.EditPost.as_view(), name='post_update'),
    path('userposts/', views.UserPosts.as_view(), name='user_posts'),
    path('userdraftposts/', views.AllDraftPosts.as_view(), name='user_draft_posts'),
    path('userarchiveposts/', views.AllArchivePosts.as_view(), name='user_archive_posts'),
    path('allposts/', views.AllUserPosts.as_view(), name='all_posts'),
    
    path('userspecific/draftposts/', views.UserSpecificDraftPosts.as_view(), name='user_spec_draft_posts'),
    path('userspecific/archiveposts/', views.UserSpecificArchivePosts.as_view(), name='user_spec_archive_posts'),
    path('userspecific/posts/', views.UserSpecificPosts.as_view(), name='user_spec_all_posts'),
    
    path('search/userspecific/posts/', views.SearchUserSpecificPosts.as_view(), name='search_user_spec_all_posts'),
    
]

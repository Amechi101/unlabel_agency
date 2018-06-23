from django.urls import include, path

from .views import (ProjectListView, ProjectDetailView, ClientListView, ClientDetailView, ArticleListView, ArticleDetailView)

urlpatterns = [

    path('', include(([

        path('projects/', ProjectListView.as_view(), name='projects'),

        path('project/<slug:slug>', ProjectDetailView.as_view(), name='project_detail'),
   
    ], 'unlabel_backend'), namespace='projects')),


    path('', include(([

        path('clients/', ClientListView.as_view(), name='client_list'),

        path('client/<slug:slug>', ClientDetailView.as_view(), name='client_detail'),
   
    ], 'unlabel_backend'), namespace='clients')),

    path('', include(([

        path('articles/', ArticleListView.as_view(), name='article_list'),

        path('article/<slug:slug>', ArticleDetailView.as_view(), name='article_detail'),
   
    ], 'unlabel_backend'), namespace='articles')),
]

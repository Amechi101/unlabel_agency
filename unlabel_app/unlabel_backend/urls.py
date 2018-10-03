from django.urls import include, path

from .views import ProjectListView, ProjectDetailView

urlpatterns = [

    path('', include(([

        path('projects/', ProjectListView.as_view(), name='projects'),

        path('project/<slug:slug>', ProjectDetailView.as_view(), name='project_detail'),
   
    ], 'unlabel_backend'), namespace='projects')),
]

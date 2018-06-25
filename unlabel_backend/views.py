from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy

from django.views.generic import (TemplateView, CreateView, DeleteView, DetailView, ListView, UpdateView)

from .models import Project, ProjectImage, Client, Article


class ProjectListView(ListView):
    model = Project
    
    template_name = 'projects/projects_list.html'

    def get_context_data(self, **kwargs):
        kwargs['projects'] = Project.objects.all().order_by('title')

        kwargs['results_obj'] = Project.objects.all()

        kwargs['projects_triptych'] = Project.objects.all().order_by('-created')[0:3]

        return super().get_context_data(**kwargs)


class ProjectDetailView(DetailView):
    model = Project
    
    template_name = 'projects/project_detail.html'

    def get_context_data(self, **kwargs):
        kwargs['project'] = self.get_object()

        kwargs['project_images'] = ProjectImage.objects.filter(project=self.get_object())

        kwargs['projects_triptych'] = Project.objects.exclude(title=self.get_object().title).order_by('-created')[0:3]

        return super().get_context_data(**kwargs)


class ClientListView(ListView):
    model = Client
    
    template_name = 'clients/client_list.html'

    def get_context_data(self, **kwargs):
        kwargs['clients'] = Client.objects.all().order_by('name')

        kwargs['results_obj'] = Client.objects.all()

        kwargs['clients_triptych'] = Client.objects.all().order_by('-created')[0:3]

        return super().get_context_data(**kwargs)

class ClientDetailView(DetailView):
    model = Client
    
    template_name = 'clients/client_detail.html'

    def get_context_data(self, **kwargs):
        kwargs['client'] = self.get_object()

        kwargs['clients_triptych'] = Client.objects.exclude(name=self.get_object().name).order_by('-created')[0:3]

        return super().get_context_data(**kwargs)


class ArticleListView(ListView):
    model = Article
    
    template_name = 'articles/article_list.html'

    def get_context_data(self, **kwargs):
        kwargs['articles'] = Article.objects.all().order_by('-created')

        kwargs['results_obj'] = Article.objects.all()

        return super().get_context_data(**kwargs)

class ArticleDetailView(DetailView):
    model = Article
    
    template_name = 'articles/article_detail.html'

    def get_context_data(self, **kwargs):
        kwargs['article'] = self.get_object()


        return super().get_context_data(**kwargs)

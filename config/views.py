from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy

from django.views.generic import (TemplateView, CreateView, DeleteView, DetailView, ListView, UpdateView)

from unlabel_backend.models import Project, Capability, Article, Client


class HomePageView(TemplateView):

    template_name = 'pages/home.html'

    def get_context_data(self, **kwargs):
        kwargs['projects_left'] = Project.objects.all().order_by('-created')[0:1]

        kwargs['projects_middle'] = Project.objects.all().order_by('-created')[1:2]

        kwargs['projects_right'] = Project.objects.all().order_by('-created')[2:4]

        kwargs['clients'] = Client.objects.all().order_by('-created')

        kwargs['articles'] = Article.objects.all()

        return super().get_context_data(**kwargs)


class AboutView(TemplateView):

    template_name = 'pages/about.html'

    def get_context_data(self, **kwargs):

        kwargs['capabilities'] = Capability.objects.all().order_by('name')

        return super().get_context_data(**kwargs)

from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy

from django.views.generic import TemplateView, ListView

from unlabel_app.unlabel_backend.models import Project


class HomePageView(TemplateView):

    template_name = 'pages/home.html'

    def get_context_data(self, **kwargs):
        kwargs['projects_left'] = Project.objects.all().order_by('-created')[0:1]

        kwargs['projects_middle'] = Project.objects.all().order_by('-created')[1:2]

        kwargs['projects_right'] = Project.objects.all().order_by('-created')[2:4]

        return super().get_context_data(**kwargs)

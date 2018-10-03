from django.views.generic import DetailView, ListView

from .models import Project, ProjectImage


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

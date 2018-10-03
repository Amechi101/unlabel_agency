from django.contrib import admin
from .models import Project, ProjectImage


class PhotoInline(admin.StackedInline):
    model = ProjectImage
    extra = 1


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):

	readonly_fields = ['slug',]

	inlines = [PhotoInline]

	list_display = ['title', 'client_name', 'is_active']

	search_fields = ['title',]


@admin.register(ProjectImage)
class ProjectImageAdmin(admin.ModelAdmin):

	list_display = ['project',]

	search_fields = ['project',]

from django.contrib import admin
from .models import Project, ProjectImage, Capability, Client, Article


class PhotoInline(admin.StackedInline):
    model = ProjectImage
    extra = 1


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):

	readonly_fields = ['slug',]

	inlines = [PhotoInline]

	list_display = ('title', 'client_name', 'is_active')

	search_fields = ['title',]


@admin.register(ProjectImage)
class ProjectImageAdmin(admin.ModelAdmin):

	list_display = ('project',)

	search_fields = ['project',]


@admin.register(Capability)
class CapabilityAdmin(admin.ModelAdmin):

	list_display = ('name',)

	search_fields = ['name',]


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):

	readonly_fields = ['slug',]

	list_display = ('title', 'author')

	search_fields = ['title', 'author']


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):

	readonly_fields = ['slug',]

	list_display = ('name',)

	search_fields = ['name',]

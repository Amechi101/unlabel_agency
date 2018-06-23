from django.urls import include, path
from django.contrib import admin
from django.views.generic.base import TemplateView
from .views import HomePageView, AboutView


urlpatterns = [
    
    # ADMIN
    path('admin/', admin.site.urls),

    # HOMEPAGE
    path('', HomePageView.as_view(), name='home'),

    # BACKEND
    path('', include('unlabel_backend.urls')),

    # PAGES
    path('about/', AboutView.as_view(), name="about"),
    path('contact/', TemplateView.as_view(template_name='pages/contact.html'), name="contact"),
]

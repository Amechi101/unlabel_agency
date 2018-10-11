from django.conf import settings
from django.urls import include, path
from django.contrib import admin
from django.views.generic.base import TemplateView
from django.views import defaults as default_views
from .views import HomePageView, AboutPageView


urlpatterns = [
    
    # ADMIN
    path('admin/', admin.site.urls),

    # HOMEPAGE
    path('', HomePageView.as_view(), name='home'),

    # BACKEND
    path('', include('unlabel_app.unlabel_backend.urls')),

    # PAGES
    path('about/', AboutPageView.as_view(), name="about"),
    path('contact/', TemplateView.as_view(template_name='pages/contact.html'), name="contact"),
]


if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path('400/', default_views.bad_request, kwargs={'exception': Exception('Bad Request!')}),
        path('403/', default_views.permission_denied, kwargs={'exception': Exception('Permission Denied')}),
        path('404/', default_views.page_not_found, kwargs={'exception': Exception('Page not Found')}),
        path('500/', default_views.server_error),
    ]
    if 'debug_toolbar' in settings.INSTALLED_APPS:
        import debug_toolbar
        urlpatterns = [
            path('__debug__/', include(debug_toolbar.urls)),
        ] + urlpatterns
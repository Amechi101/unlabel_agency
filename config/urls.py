from django.urls import include, path
from django.contrib import admin
from django.views.generic.base import TemplateView
from .views import homepage
from uccbackend.views.view_brands import BrandSignUpView
# from uccbackend.views.dashboard import creators


urlpatterns = [
    
    # ADMIN
    path('admin/', admin.site.urls),

    # HOME
    path('', homepage, name='home'),

    # CREATOR/BRAND LOGIN
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/brands/', BrandSignUpView.as_view(), name='brand_signup'),
    # path('accounts/signup/creator/', creators.CreatorSignUpView.as_view(), name='creator_signup'),

    # BRAND/CREATOR ACCOUNTS
    path('', include('uccbackend.urls')),

    # PAGES
    path('faq/', TemplateView.as_view(template_name='pages/faq.html'), name="faq"),
]

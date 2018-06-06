from django.urls import include, path

from .views import creators

urlpatterns = [

    path('dashboard/', include(([
        
        path('', brands.ProductListView.as_view(), name='dashboard_home'),
   
    ], 'uccbackend'), namespace='brands')),
]
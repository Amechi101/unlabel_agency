from django.urls import include, path

# from .views import view_creators
from .views import view_brands

urlpatterns = [

    # path('', include(([

    #     path('profile/', creators.CreatorProfileView.as_view(), name='profile_info'),

    #     path('profile/account/', creators.AccountView.as_view(), name='account_info'),

    #     path('profile/physical-attributes/', creators.CreatorPhysicalAttributesView.as_view(), name='profile_physical_attributes'),

    #     path('profile/product-preferences/', creators.CreatorProductPreferencesView.as_view(), name='profile_product_preferences'),

    #     path('profile/shipping-address/', creators.CreatorShippingAddressView.as_view(), name='profile_shipping_address'),

    #     path('settings/password/', creators.change_password, name='change_password'),

    #     path('products/', creators.ProductsListView.as_view(), name='products_list'),

    #     path('products/<int:pk>/', creators.ProductDetailView.as_view(), name='product_detail'),
        
    #     path('products/selected/', creators.SelectedProductsListView.as_view(), name='selected_products'),
        
    #     path('products/review/<int:pk>/', creators.CreateProductReviewView.as_view(), name='product_review_create'),

    #     path('products/reviewed/', creators.CompletedProductReviewListView.as_view(), name='complete_product_reviews'),
        
    # ], 'uccbackend'), namespace='creators')),


    path('dashboard/', include(([

        path('', view_brands.DashboardView.as_view(), name='dashboard'),

        path('settings/profile/', view_brands.BrandInfoView.as_view(), name='brand_info'),

        path('settings/account/', view_brands.BrandAccountView.as_view(), name='account_info'),

        path('settings/password/', view_brands.change_password, name='change_password'),
        
        path('products/', view_brands.ProductListView.as_view(), name='products_list'),

        path('products/create/', view_brands.CreateProductView.as_view(), name='create_product'),
   
    ], 'uccbackend'), namespace='brands')),
]

from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = ('pk', 'name', 'brand',)

    search_fields = ['brand']

# @admin.register(ProductCategory)
# class ProductCategoryAdmin(admin.ModelAdmin):

#     list_display = ('name',)

#     search_fields = ['name']


# @admin.register(ProductSelected)
# class ProductSelectedAdmin(admin.ModelAdmin):

#     list_display = ('creator', 'product',)

#     search_fields = ['creator']


# @admin.register(ProductReview)
# class ProductReviewAdmin(admin.ModelAdmin):

#     list_display = ('pk', 'product')

#     search_fields = ['product']




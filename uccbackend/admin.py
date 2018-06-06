from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import User, ShippingAddress, Creator, Brand


class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User


class MyUserCreationForm(UserCreationForm):

    error_message = UserCreationForm.error_messages.update({
        'duplicate_username': 'This username has already been taken.'
    })

    class Meta(UserCreationForm.Meta):
        model = User

    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['duplicate_username'])


@admin.register(User)
class MyUserAdmin(AuthUserAdmin):
    form = MyUserChangeForm
    add_form = MyUserCreationForm
    fieldsets = (
            ('User Profile', {'fields': ('first_name', 'is_creator', 'is_brand',)}),
    ) + AuthUserAdmin.fieldsets
    list_display = ('username', 'first_name', 'is_superuser', 'is_brand', 'is_creator')
    search_fields = ['first_name']


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):

    list_display = ('user',)

    search_fields = ['user']


@admin.register(Creator)
class CreatorAdmin(admin.ModelAdmin):

    list_display = ('user',)

    search_fields = ['user']


@admin.register(ShippingAddress)
class ShippingAddressAdmin(admin.ModelAdmin):

    list_display = ('creator', 'summary')

    search_fields = ['creator',]

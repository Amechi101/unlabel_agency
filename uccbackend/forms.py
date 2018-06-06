from django import forms
from django.db import transaction
from django.contrib.auth.forms import UserCreationForm

from uccbackend.models import (User, ShippingAddress, Brand, Product)


DOY = ('1960', '1961', '1962','1963', '1964', '1965', '1966', '1967','1968', 
        '1969', '1970', '1971', '1972','1973', '1974', '1975', '1976', '1977',
        '1978', '1979','1980', '1981', '1982', '1983', '1984', '1985', '1986', 
        '1987','1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995',
        '1996', '1997', '1998', '1999', '2000')


class BrandSignUpForm(UserCreationForm):

    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=254, help_text='Enter a valid email address.')
    
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_brand = True
        user.save()
        
        brand = Brand.objects.create(user=user)
        
        return user


class BrandProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BrandProfileForm, self).__init__(*args, **kwargs)
        
        # required fields
        self.fields['name'].required = True
        self.fields['description'].required = True
        self.fields['image'].required = True
        self.fields['website'].required = True
        self.fields['image'].required = True
        self.fields['city'].required = True
        self.fields['country'].required = True
        self.fields['audience'].required = True

        # error messages
        self.fields['image'].error_messages = 'You have exceed 10MB! Please upload something less than 10MB'

    class Meta:
        model = Brand
        fields = (
            'name', 
            'description', 
            'image',
            'website',
            'city', 
            'state', 
            'country',
            'audience',
        )


class BrandAccountForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BrandAccountForm, self).__init__(*args, **kwargs)
        
        self.fields['email'].required = True
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['username'].required = True
    
    class Meta:
        model = User
        fields = ('email', 'username', 'first_name', 'last_name')


class CreateProductForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(CreateProductForm, self).__init__(*args, **kwargs)

        # required fields
        self.fields['title'].required = True
        self.fields['price'].required = True
        self.fields['description'].required = True
        self.fields['url'].required = True
        self.fields['category'].required = True
        self.fields['image'].required = True
        self.fields['product_gender_type'].required = True
        self.fields['campaign_type'].required = True

    
    class Meta:
        model = Product
        fields = (
            'title',
            'price', 
            'description', 
            'url', 
            'category',
            'image',
            'product_gender_type',  
            'campaign_type',
        )
   

from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import (TemplateView, CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from ..decorators import brand_required
from ..forms import (BrandSignUpForm, BrandProfileForm, BrandAccountForm, CreateProductForm)
from ..models import User, Brand, Product



class BrandSignUpView(CreateView):
    model = User
    form_class = BrandSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'brand'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('brands:dashboard')


@method_decorator([login_required, brand_required], name='dispatch')
class DashboardView(TemplateView):

    template_name = 'dashboard/brands/home_dashboard.html'

    def get_context_data(self, **kwargs):

        kwargs['active_tab'] = 'dashboard'
        kwargs['page_title'] = 'Unlabel Brand Dashboard'

        return super().get_context_data(**kwargs)


@method_decorator([login_required, brand_required], name='dispatch')
class BrandInfoView(UpdateView):
    model = Brand
    form_class = BrandProfileForm
    template_name = 'dashboard/brands/settings/profile_edit.html'
    success_url = reverse_lazy('brands:brand_info')

    def get_object(self):
        return self.request.user.brand

    def get_context_data(self, **kwargs):
        kwargs['brand_data'] = Brand.objects.filter(user=self.request.user)
        kwargs['active_tab'] = 'brand_info'
        kwargs['page_title'] = 'Brand Info'

        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        messages.success(self.request, 'Profile Info updated!')
        return super().form_valid(form)

@method_decorator([login_required, brand_required], name='dispatch')
class BrandAccountView(UpdateView):
    model = User
    form_class = BrandAccountForm
    template_name = 'dashboard/brands/settings/default_edit.html'
    success_url = reverse_lazy('brands:account_info')

    def get_object(self):
        return self.request.user

    def get_context_data(self, **kwargs):
        kwargs['active_tab'] = 'account_info'
        kwargs['page_title'] = 'Account Info'

        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        messages.success(self.request, 'Account Info updated!')
        return super().form_valid(form)

@login_required
@brand_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('brands:change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'dashboard/brands/settings/default_edit.html', {
        'form': form,
        'active_tab':'password',
        'page_title':'Settings'
    })


@method_decorator([login_required, brand_required], name='dispatch')
class ProductListView(ListView):
    model = Product
    ordering = ('title', )
    context_object_name = 'products'
    template_name = 'dashboard/brands/products/products_list.html'


    def get_context_data(self, **kwargs):
        kwargs['active_tab'] = 'products'
        kwargs['page_title'] = 'Products'

        return super().get_context_data(**kwargs)

    # def get_queryset(self):
    #     queryset = self.request.user.products \
    #         .select_related('subject')
    #     return queryset


@method_decorator([login_required, brand_required], name='dispatch')
class CreateProductView(CreateView):
    model = Product

    form_class = CreateProductForm
    
    template_name = 'dashboard/brands/products/create_product_form.html'

    success_url = reverse_lazy('brands:products_list')
    
    def form_valid(self, form):

        product = form.save(commit=False)

        product.save()
        
        messages.success(self.request, 'Product' + ' ' + product.title)

        return super().form_valid(form)

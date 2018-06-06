from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from ...decorators import brand_required
from ...forms import BrandSignUpForm
from ...models import User, Brand, Product


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
        return redirect('brands:dashboard_home')


@method_decorator([login_required, brand_required], name='dispatch')
class ProductListView(ListView):
    model = Product
    ordering = ('name', )
    context_object_name = 'products'
    template_name = 'dashboard/brands/dashboard.html'

    # def get_queryset(self):
    #     queryset = self.request.user.products \
    #         .select_related('subject')
    #     return queryset



from django.contrib import messages
from django.template import loader
from django.core.mail import send_mail, mail_admins, send_mass_mail
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.db.models import Q
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, UpdateView, TemplateView, DetailView

from datetime import datetime, timedelta

from ...decorators import creator_required
from ...forms import (CreatorSignUpForm, CreatorProfileForm, AccountForm, CreatorShippingAddressForm, ProductReviewForm, CreatorPhysicalAttributesForm, CreatorProductPreferencesForm)
from ...models import User, Creator, Brand, Product, ShippingAddress, ProductSelected, ProductReview


class CreatorSignUpView(CreateView):
    model = User
    form_class = CreatorSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'creator'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('creators:profile_info')


@method_decorator([login_required, creator_required], name='dispatch')
class CreatorProfileView(UpdateView):
    model = Creator
    form_class = CreatorProfileForm
    template_name = 'dashboard/creators/account/profile_edit.html'
    success_url = reverse_lazy('creators:profile_info')

    def get_object(self):
        return self.request.user.creator

    def get_context_data(self, **kwargs):
        kwargs['active_tab'] = 'profile_info'
        kwargs['page_title'] = 'Profile Info'

        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        messages.success(self.request, 'Profile Info updated!')
        return super().form_valid(form)


@method_decorator([login_required, creator_required], name='dispatch')
class CreatorPhysicalAttributesView(UpdateView):
    model = Creator
    form_class = CreatorPhysicalAttributesForm 
    template_name = 'dashboard/creators/account/profile_edit.html'
    success_url = reverse_lazy('creators:profile_physical_attributes')

    def get_object(self):
        return self.request.user.creator

    def get_context_data(self, **kwargs):
        kwargs['active_tab'] = 'physical_attributes'
        kwargs['page_title'] = 'Physical Attributes'

        return super().get_context_data(**kwargs)


    def form_valid(self, form):
        messages.success(self.request, 'Physical Attributes updated!')
        return super().form_valid(form)


@method_decorator([login_required, creator_required], name='dispatch')
class CreatorProductPreferencesView(UpdateView):
    model = Creator
    form_class = CreatorProductPreferencesForm
    template_name = 'dashboard/creators/account/profile_edit.html'
    success_url = reverse_lazy('creators:profile_product_preferences')

    def get_object(self):
        return self.request.user.creator

    def get_context_data(self, **kwargs):
        kwargs['active_tab'] = 'product_preferences'
        kwargs['page_title'] = 'Product Preferences'

        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        messages.success(self.request, 'Product Preferences updated!')
        return super().form_valid(form)


@method_decorator([login_required, creator_required], name='dispatch')
class CreatorShippingAddressView(UpdateView):
    model = ShippingAddress
    form_class = CreatorShippingAddressForm
    template_name = 'dashboard/creators/account/profile_edit.html'
    success_url = reverse_lazy('creators:profile_shipping_address')

    def get_object(self):
        
        return self.request.user.creator.shipping_addresses

    def get_context_data(self, **kwargs):
        kwargs['active_tab'] = 'addresses'
        kwargs['page_title'] = 'Shipping Address'

        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        messages.success(self.request, 'Shipping Address updated!')
        return super().form_valid(form)


@method_decorator([login_required, creator_required], name='dispatch')
class AccountView(UpdateView):
    model = User
    form_class = AccountForm
    template_name = 'dashboard/creators/account/profile_edit.html'
    success_url = reverse_lazy('creators:account_info')

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
@creator_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('creators:change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'dashboard/creators/account/profile_edit.html', {
        'form': form,
        'active_tab':'password',
        'page_title':'Settings'
    })



@method_decorator([login_required, creator_required], name='dispatch')
class ProductsListView(ListView):
    model = Product
    ordering = ('name', )
    context_object_name = 'products'
    template_name = 'dashboard/creators/products/product_list.html'

    def get_context_data(self, **kwargs):
        kwargs['active_tab'] = 'available_products'
        kwargs['page_title'] = 'Available Products'

        return super().get_context_data(**kwargs)


    def get_queryset(self):
        creator = self.request.user.creator
 
        creator_interests = creator.interests.values_list('pk', flat=True)

        creator_sex = creator.sex
        
        creator_selected_products = creator.interested_product.values_list('product', flat=True)
        
        queryset = Product.objects.filter(category__in=creator_interests) \
            .filter(Q(gender=creator_sex) | Q(gender__contains='UNISEX')) \
            .exclude(pk__in=creator_selected_products)
        return queryset


@method_decorator([login_required, creator_required], name='dispatch')
class ProductDetailView(DetailView):
    model = Product
    
    template_name = 'dashboard/creators/products/product_detail.html'

    def get_context_data(self, **kwargs):
        kwargs['product'] = self.get_object()

        return super().get_context_data(**kwargs)

    def post(self, request, *args, **kwargs):

        current_user = self.request.user
        creator = current_user.creator
        product = Product.objects.get(pk=self.kwargs['pk'])
       
        selected_product = ProductSelected.objects.create(creator=creator, product=product)

        creator_subject, creator_from_email, creator_to =  product.name + ' selected', 'creators@unlabel.us', current_user.email

        admin_subject, admin_to = product.name + ' selected' + ' by' + current_user.username, 'info@unlabel.us'
        
        creator_html_message = loader.render_to_string(
            'dashboard/creators/products/partials/selected_product_email_to_creator.html',
            {
                'product_name': product.name,
                'brand_name':  product.brand,
            }
        )

        admin_html_message = loader.render_to_string(
            'dashboard/creators/products/partials/selected_product_email_to_admin.html',
            {
                'product_name': product.name,
                'brand_name':  product.brand,
                'first_name':  current_user.first_name,
                'last_name':  current_user.last_name,
                'username':  current_user.username,
            }
        )

        send_mail(creator_subject, '', creator_from_email, [creator_to], fail_silently=False, connection=None, html_message=creator_html_message)

        send_mail(admin_subject, '', creator_from_email, [admin_to], fail_silently=False, connection=None, html_message=admin_html_message)
       
        messages.success(self.request, 'Product selected with success! We will send you an email with next steps.')
        
        return redirect('creators:selected_products')


@method_decorator([login_required, creator_required], name='dispatch')
class SelectedProductsListView(ListView):
    model = Product
    
    context_object_name = 'selected_products_obj'
    
    template_name = 'dashboard/creators/products/selected_products_list.html'

    def get_context_data(self, **kwargs):
        kwargs['active_tab'] = 'selected_products'
        kwargs['page_title'] = 'Selected Products'

        return super().get_context_data(**kwargs)

    def get_queryset(self):
        '''
        This method is an implicit object-level permission management
        This view will only match the ids of existing selected products that belongs
        to the logged in creator.
        '''
        creator = self.request.user.creator

        creator_selected_products = creator.interested_product.values_list('product', flat=True)
        
        creator_reviewed_products = creator.reviewed_product.values_list('product', flat=True)
        
        queryset = Product.objects.filter(pk__in=creator_selected_products) \
            .exclude(pk__in=creator_reviewed_products)
        return queryset


@method_decorator([login_required, creator_required], name='dispatch')
class CreateProductReviewView(CreateView):
    model = ProductReview

    form_class = ProductReviewForm
    
    template_name = 'dashboard/creators/products/product_review_form.html'

    success_url = reverse_lazy('creators:complete_product_reviews')

    def get_context_data(self, **kwargs):
        kwargs['product'] = Product.objects.get(pk=self.kwargs['pk'])

        return super().get_context_data(**kwargs)
    
    def form_valid(self, form):

        current_creator = Creator.objects.get(user=self.request.user)

        selected_product = Product.objects.get(pk=self.kwargs['pk'])

        product_review = form.save(commit=False)

        product_review.product = selected_product

        product_review.creator = current_creator

        product_review.save()
        
        messages.success(self.request, 'Product review complete!')

        return super().form_valid(form)


@method_decorator([login_required, creator_required], name='dispatch')
class CompletedProductReviewListView(ListView):
    model = ProductReview
    
    context_object_name = 'complete_product_reviews'
    template_name = 'dashboard/creators/products/complete_product_reviews_list.html'

    def get_queryset(self):
        '''
        This method is an implicit object-level permission management
        This view will only match the ids of existing reviewed products that belongs
        to the logged in creator.
        '''

        return self.request.user.creator.reviewed_product.all()


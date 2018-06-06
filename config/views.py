from django.shortcuts import redirect, render
from django.views.generic import TemplateView


def homepage(request):
    if request.user.is_authenticated:
        if request.user.is_brand:
            return redirect('brands:dashboard')
        else:
            return redirect('creators:profile_info')
    return render(request, 'pages/home.html')

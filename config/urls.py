"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path
from django.views.generic.base import TemplateView

from app import views as app_views

urlpatterns = [
    # path('', app_views.index, name='index'),
    path('', TemplateView.as_view(template_name='app/index.html'), name='index'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('home/', TemplateView.as_view(template_name='app/home.html'), name='home'),
    # path('home/', app_views.home, name='home'),
    # path('join/', app_views.join, name="signup"),
    path('join/', app_views.SignUpView.as_view(), name="signup"),
]

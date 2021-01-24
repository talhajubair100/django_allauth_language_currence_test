"""djauth URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from .views import *
from acc.views import *
from django.conf.urls.i18n import i18n_patterns 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
    path('selectcurrency', selectcurrency, name='selectcurrency'),
    path('accounts/', include('allauth.urls')),
    path('', include('acc.urls')),
    path('currencies/', include('currencies.urls')),
    path('b_code/', include('b_code.urls')),

    #path('accounts/signup/company/', AccountSignupView.as_view(), name='company_signup'),
    #path('accounts/signup/company/', teachers.TeacherSignUpView.as_view(), name='company_signup'),
]




urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

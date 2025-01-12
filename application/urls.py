"""
URL configuration for Brotomotiv project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from application import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('about/', views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('ceramic/',views.ceramic,name='ceramic'),
    path('ppf/',views.ppf,name='ppf'),
    path('detailing/',views.detailing,name='detailing'),
    path('insurance/',views.insurance,name='insurance'),
    path('denting/',views.denting,name='denting'),
    path('wrap/',views.wrap,name='wrap'),
    path('other/',views.other,name='other'),
#login,admin URLS 
    path('login/', views.admin_login, name='login'),
    path('logout/',views.logout_user, name='logout'),
    path('master_page/',views.master_page, name='master_page'),
    
]

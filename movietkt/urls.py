"""movietkt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls.static import static
from django.urls import path
from tktapp import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup',views.Sign),
    path('login',views.login),
    path('',views.home),
    path('m',views.movie),
    path('l',views.mlist),
    path('t',views.theatre),
    path('tl',views.thlist),
    path('bk',views.booking),
    path('tk',views.ticket),
    path('st',views.seatl),
    path('lt',views.layout),
    path('ly',views.location)
] 
static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

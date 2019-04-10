"""swiper URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from user import api as user_api

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'usr/api/submit_phone', user_api.submit_phone),
    url(r'usr/api/submit_vcode', user_api.submit_vcode),
    url(r'usr/api/get_profile', user_api.get_profile),
    url(r'usr/api/set_profile', user_api.set_profile),
    url(r'usr/api/upload_avatar', user_api.upload_avatar),
]
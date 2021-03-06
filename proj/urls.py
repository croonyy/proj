"""proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import include, path, re_path
# from django.conf.urls import url
# from django.conf.global_settings import STATICFILES_DIRS
from django.conf import settings
# from proj import settings
from django.views.static import serve
import os

print('STATIC_URL' + str(settings.STATIC_URL))
print('STATIC_ROOT' + str(settings.STATIC_ROOT))
print('STATICFILES_DIRS' + str(settings.STATICFILES_DIRS))

static_url = r'^{}/(?P<path>.*)$'.format(settings.STATIC_URL.replace('/', ''))
print('static url server:' + str(static_url))

urlpatterns = [
    # 配置静态文件代理
    re_path(static_url, serve, {'document_root': settings.STATIC_ROOT}),
    path('admin/', admin.site.urls),
    path('insight/', include('insight.urls')),
]

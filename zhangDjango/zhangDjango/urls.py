"""zhangDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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

from blog import views

urlpatterns = [

    url(r'^blog/(\d+)/$', views.hello),  # 正则表达式 2b了 \d+ 其中的\ 是不能省略的~ 和\\d对比一下~

    url(r'^blog/', views.hello1),

    url(r'^admin/', admin.site.urls),

    url(r'^index/', views.index)
]

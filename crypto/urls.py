"""crypto URL Configuration

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
from django.urls import include, path
from django.conf import settings
from django.shortcuts import render
from routes.main import time, add_list, delete_list, update_list, query_list, page_not_font
from django.views.static import serve
import app

urlpatterns = [
    # 分别是两个必选参数：route、view 和两个可选参数：kwargs、name。
    # '''
    # path(route, view, kwargs=None, name=None)
    # route: 字符串，表示 URL 规则，与之匹配的 URL 会执行对应的第二个参数 view。
    # view: 用于执行与正则表达式匹配的 URL 请求。
    # kwargs: 视图使用的字典类型的参数。
    # name: 用来反向获取 URL。
    # '''
    # path('admin/', admin.site.urls),
    # path('', time),
    path(r'uploads/*', serve, {"document_root": settings.MEDIA_ROOT, }),
    path('', include('app.urls')),
    path(r'add_list/', add_list),
    path(r'delete_list/', delete_list),
    path(r'update_list/', update_list),
    path(r'query_list/', query_list),
    path(r'<int:question_id>/vote/', query_list),
    path(r'app/', include(app.urls))
]


"""bank URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from trans import views



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^trans/$', views.TransListView.as_view(), name='all_trans'),
    url(r'^trans/add/$', views.tr_add),
    url(r'^trans/(?P<pk>\w+)/$', views.TransactDetail.as_view(), name='one_tr'),
    url(r'^trans/edit/(?P<pk>\w+)/$', views.tr_edit, name='trans_edit'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^logout/$', views.u_logout, name='logout'),
    url(r'^login/$', views.u_login, name='login'),
    url(r'^page/(?P<page>\d+)/$', views.TransListView.as_view()),
]

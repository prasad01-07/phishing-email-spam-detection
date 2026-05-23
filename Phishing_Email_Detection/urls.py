"""Phishing_Email_Detection URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from Phishing_Email_Detection import settings
from Users import views as userview
from Admins import views as admin_views

urlpatterns = [
    url('admin/', admin.site.urls),


    url('^$',userview.userlogin,name="userlogin"),
    url('^userregister/$',userview.userregister,name="userregister"),
    url('^mydetails/$',userview.mydetails,name="mydetails"),
    url('^userpage/$', userview.userpage, name="userpage"),
    url('^checking/$', userview.checking, name="checking"),
    url('^checking_attack/$', userview.checking_attack, name="checking_attack"),
    url('^viewmailpage/$',userview.viewmailpage,name="viewmailpage"),
    url('user/spampage',userview.spampage,name="spampage"),
    url('user/delete/(?P<pk>\d+)/$',userview.deleteobj,name="deleteobj"),
    url('user/spamdelete/(?P<pk>\d+)/$',userview.spamdeleteobj,name="spamdeleteobj"),
    url('user/feedback', userview.feedback, name="feedback"),


    url('admin/login_page',admin_views.login_page,name="login_page"),
    url('admin_page',admin_views.admin_page,name="admin_page"),
    url('analysis_page',admin_views.analysis_page,name="analysis_page"),
    url('categoryanalysis/(?P<chart_type>\w+)',admin_views.categoryanalysis_chart,name="categoryanalysis_chart"),
    url('admin/delete/(?P<pk>\d+)/$',admin_views.analysisdelete,name="analysisdelete"),
    url('admin/viewfeedback', admin_views.viewfeedback, name="viewfeedback"),
    url('admin/attactdetails', admin_views.attactdetails, name="attactdetails"),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

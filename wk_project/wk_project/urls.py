"""wk_project URL Configuration

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
from django.contrib import admin
from django.urls import path
from twitter.views import SignInView, LogInView, AllMsgsView, NewMessView, NewCommentView, FollowUserView

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', AllMsgsView.as_view(), name='main'),
    url(r'^register/$', SignInView.as_view(), name='sign-in'),
    url(r'^login/$', LogInView.as_view(), name='login'),
    url(r'^msg/(?P<msg_id>(\d+))/new-comment/$', NewCommentView.as_view(), name='new-comment'),
    url(r'^user/(?P<user_id>(\d+))/follow', FollowUserView.as_view(), name='follow-user'),
    url(r'^msg/new/$', NewMessView.as_view(), name='new-msg')

]

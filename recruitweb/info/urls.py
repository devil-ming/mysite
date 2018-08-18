from django.conf.urls import url, include
from .views import *

urlpatterns = [
    url(r"^register/$", register_views),
    url(r'^index/$', index_views),
    url(r'^login/$',login_views),
    url(r'^logout',logout_views),
    url(r'^confirm/$',user_confirm),
    url(r'^captcha', include('captcha.urls')),
]
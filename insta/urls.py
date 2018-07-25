from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$',views.home,name='home'),
    url(r'^newprofile/',views.profile,name ='profile'),
    url(r'^showprofile/(?P<id>\d+)',views.display_profile,name = 'showprofile'),
    url(r'^image/$', views.add_image, name='upload_image'),
    url(r'^ search/',views.search, name='search'),
    url(r'^comment/(?P<image_id>\d+)', views.comment, name='comment'),

]
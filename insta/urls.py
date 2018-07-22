from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$',views.home,name='home'),
    url(r'^newprofile/',views.profile,name = 'profile'),
    url(r'^showprofile/(\d+)',views.display_profile,name = 'showprofile'),

]
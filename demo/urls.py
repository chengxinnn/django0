from django.conf.urls import url
from . import views


app_name = 'demo'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^page/(?P<p_id>[0-9]{0,4})', views.detail, name='detail'),
    url(r'^add/$', views.add, name='add'),
    url(r'^add/(\d+)/(\d+)$',views.add2, name='add2'),
    url(r'^type/$', views.type, name='form'),
    url(r'^typetest/$', views.typetest, name='formtest'),

]
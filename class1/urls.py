from django.conf.urls import url
from . import views

app_name = 'class1'

urlpatterns = [
    url(r'^login/$', views.login, name='login'),
    url(r'^main/$', views.main, name='main'),
    url(r'^index/$', views.index, name='index'),
    url(r'^list/$', views.list_model, name='index'),
    url(r'^list1/$', views.list_sql, name='index'),

]
from django.contrib import admin
from .models import Bookinfo, Bookhouse, Booktype, Users
from . import views
import xadmin
from xadmin import views


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True

class GlobalSettings(object):
    site_title = '课程教学平台'
    site_footer = '杰普软件'

xadmin.site.register(views.BaseAdminView,BaseSetting)
xadmin.site.register(views.CommAdminView,GlobalSettings)

# Register your models here.
xadmin.site.register(Booktype)
xadmin.site.register(Bookinfo)
xadmin.site.register(Bookhouse)
xadmin.site.register(Users)
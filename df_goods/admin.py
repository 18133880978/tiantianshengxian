from django.contrib import admin
from .models import *


class TypeInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'ttitle', 'isDelete']


class GoodsInfoAdmin(admin.ModelAdmin):
    list_per_page = 20
    actions_on_bottom = True
    list_display = ['id', 'gtitle', 'gprice', 'gunit', 'gtype_id', 'gstk', 'gpic', 'gintroduce',
                    'gcontent', 'gclick', 'gadv', 'isDelete']

# Register your models here.
admin.site.register(TypeInfo, TypeInfoAdmin)
admin.site.register(GoodsInfo, GoodsInfoAdmin)
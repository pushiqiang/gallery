# -*- coding:utf-8 -*-
from django.contrib import admin
from photo.models import Item,Photo
# Register your models here.

class PhotoAdmin(admin.ModelAdmin):
    fieldsets = [
	[u'标题',{"fields":("item","title"),"description":u"图片的相册名和标题","classes":("collapse",)}],
	[u'图片',{"fields":("image","caption")}]
    ]


class PhotoInline(admin.StackedInline):
    model = Photo

class ItemAdmin(admin.ModelAdmin):
    inlines = [PhotoInline]

admin.site.register(Item,ItemAdmin)
admin.site.register(Photo,PhotoAdmin)

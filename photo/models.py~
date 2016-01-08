#-*- coding:utf-8 -*-
from django.db import models
from items.fields import ThumbnailImageField

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=250,verbose_name=u'相册名')
    description = models.TextField(verbose_name=u'描述')

    class Meta:
        ordering = ['name']
        verbose_name_plural = u'相册'
        #app_label = u'相册'

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('item_detail',None,{'pk':int(self.id)})

class Photo(models.Model):
    item = models.ForeignKey(Item)
    title = models.CharField(max_length=100,verbose_name=u'标题')
    image = ThumbnailImageField(upload_to='photos',verbose_name=u'照片')
    caption = models.CharField(max_length=250,blank=True,verbose_name=u'字幕')

    class Meta:
        ordering = ['title']
        verbose_name_plural = u'照片'
        #app_label = u'相册'
    
    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('photo_detail',None,{'pk':int(self.id)})






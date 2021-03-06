from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

from django.contrib.staticfiles.urls import staticfiles_urlpatterns


from photo.views import IndexView,ItemListView,ItemDetailView,PhotoDetailView

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gallery.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$',IndexView.as_view(), name='index'),
    url(r'^items/$', ItemListView.as_view(),name='items_list'),
    url(r'^items/(?P<pk>\d+)/$',ItemDetailView.as_view() ,name='item_detail'),
    url(r'^photos/(?P<pk>\d+)/$',PhotoDetailView.as_view() ,name='photo_detail'),

    url(r'^admin/', include(admin.site.urls)),

    
)

#urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += patterns('',
    
    url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),
    
)



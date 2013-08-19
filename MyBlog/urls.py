from django.conf.urls import patterns, include, url
from Blog.MyFeed import LatestEntriesFeed
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'MyBlog.views.home', name='home'),
    #url(r'^MyBlog/', include('MyBlog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^feed$', LatestEntriesFeed()),
)

urlpatterns += patterns('Blog.views',
                        url(r'^category/(.*)/$','Categorylist'),
                        url(r'search','Search'),
                        url(r'^(.*)/$','Page'),
                        url(r'^$','Index'),
                        url(r'^checkout$','article_out')
                        )

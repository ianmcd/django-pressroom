from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'press.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^press/', include('pressapp.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

from django.conf.urls import include, url
from django.contrib import admin
from django.http import HttpResponse

urlpatterns = [
    # Examples:
    # url(r'^$', 'ask.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'qa.views.test'),
    url(r'^login/$', 'qa.views.test'),
    url(r'^signup/$', 'qa.views.test'),
    url(r'^question/[0-9]*/$', 'qa.views.test'),
    url(r'^ask/$', 'qa.views.test'),
    url(r'^popular/$', 'qa.views.test'),
    url(r'^new/[0-9]*/$', 'qa.views.test'),
]

from django.conf.urls import include, url
# from django.contrib import admin
from django.http import HttpResponse

urlpatterns = [
    # Examples:
    # url(r'^$', 'ask.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'qa.views.main', name='qa-main'),
    url(r'^login/$', 'qa.views.login', name='qa-login'),
    url(r'^signup/$', 'qa.views.signup', name='qa-signup'),
    url(r'^question/(?P<id>\d+)/$', 'qa.views.question', name='qa-question'),
    url(r'^ask/', 'qa.views.ask', name='qa-ask'),
    url(r'^popular/', 'qa.views.popular', name='qa-popular'),
    url(r'^new/$', 'qa.views.test'),
    # url(r'^answer/$', 'qa.views.answer', name='qa-answer'),
]

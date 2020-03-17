from django.conf.urls import url
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import views as django_auth_views

urlpatterns = [
    url('^$', django_auth_views.password_reset, {
        'post_reset_redirect': reverse_lazy('password_reset_done')},
        name='password_reset'),
    url(r'^done/$', django_auth_views.password_reset_done,
        name='password_reset_done'),
    url(r'^(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
        django_auth_views.password_reset_confirm,
        {'post_reset_redirect': reverse_lazy('password_reset_complete')},
        name='password_reset_confirm'),
    url(r'^complete/$', django_auth_views.password_reset_complete,
        name='password_reset_complete')
]

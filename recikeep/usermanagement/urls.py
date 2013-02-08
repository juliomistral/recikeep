from django.conf.urls import patterns

from .views import handle_signup

urlpatterns = patterns('',
    (r'^signup$', handle_signup),
)
from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required
from intranet import views as iv
from django.conf import settings
urlpatterns=[
	url(r'^$', iv.HomePageView.as_view()),
	url(r'^home/$', login_required(iv.HomePageView.as_view())),
        url(r'^posts/$',login_required(iv.PostPageView.as_view())),
]
if settings.SERVE_MEDIA:
	urlpatterns += (
		url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.STATIC_ROOT}),
		url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT})
)

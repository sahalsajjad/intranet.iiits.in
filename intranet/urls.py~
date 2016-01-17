from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required
from intranet import views as iv, functions
from django.conf import settings
urlpatterns=[
	url(r'^$', login_required(iv.HomePageView.as_view())),
        url(r'^posts/$',login_required(iv.PostPageView.as_view())),
	url(r'^news/$',login_required(iv.NewsPageView.as_view())),
	url(r'^notices/$',login_required(iv.NoticePageView.as_view())),
	url(r'^resources/$',login_required(iv.ResourcesPageView.as_view())),
	url(r'^suggestions/$',login_required(iv.SuggestionsPageView.as_view())),
	url(r'^accounts/login/$',iv.LoginView.as_view()),
	url(r'^events/$',login_required(iv.ResourcesPageView.as_view())),
	url(r'^visits/$',login_required(iv.ResourcesPageView.as_view())),
	url(r'^clubs/$',login_required(iv.ResourcesPageView.as_view())),
	url(r'^committees/$',login_required(iv.ResourcesPageView.as_view())),
	url(r'^about/$',login_required(iv.ResourcesPageView.as_view())),
	url(r'^comment_to_posts/$',login_required(functions.post_comment))
]
if settings.SERVE_MEDIA:
	urlpatterns += (
		url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.STATIC_ROOT}),
		url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT})
)

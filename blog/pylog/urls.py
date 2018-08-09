from django.urls import path, re_path
from . import views
from .feeds import LatestPostFeed

app_name = 'pylog'

urlpatterns = [
    path('', views.portfolio, name='portfolio'),
    path('pylog/', views.post_list, name='post_list'),
    path('tag/<slug:tag_slug>/', views.post_list, name='post_list_by_tag'),
    # re_path(r'^$', views.PostListView.as_view(), name='post_list'),
    re_path(
        r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$',
        views.post_detail,
        name='post_detail'),
    re_path(r'^(?P<post_id>\d+)/share/$', views.post_share, name='post_share'),
    path('feed/', LatestPostFeed(), name='post_feed'),
]

#from django.conf.urls.defaults import patterns, url
from podcasting.views import (ShowListView, ShowDetailView, EpisodeListView,
                              EpisodeDetailView, sub_categories_per_main_category)
from django.conf.urls import patterns, url, include


urlpatterns = patterns("",
    url(r"^$", ShowListView.as_view(),
        name="podcasting_show_list"),
    url(r"^(?P<slug>[-\w]+)/$", ShowDetailView.as_view(),
        name="podcasting_show_detail"),
    url(r"^(?P<show_slug>[-\w]+)/archive/$", EpisodeListView.as_view(),
        name="podcasting_episode_list"),
    url(r"^(?P<show_slug>[-\w]+)/(?P<slug>[-\w]+)/$", EpisodeDetailView.as_view(),
        name="podcasting_episode_detail"),
    url('^category-filter/(?P<main_category_id>\d+)/(?P<show_id>\d+)/$',
        sub_categories_per_main_category, name="sub_categories_per_main_category"),
)

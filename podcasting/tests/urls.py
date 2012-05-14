from django.conf.urls.defaults import *

urlpatterns = patterns("",
    url(r"^podcasts/", include("podcasting.urls")),
    url(r"^podcasts/feeds/", include("podcasting.urls_feeds")),
    )

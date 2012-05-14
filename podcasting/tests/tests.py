from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from django.conf import settings

from milkman.dairy import milkman

from podcasting.models import Show, Episode, Enclosure


class PodcastTests(TestCase):
    def setUp(self):
        settings.ROOT_URLCONF = 'podcasting.tests.urls'
        self.show = milkman.deliver(
            Show, title="snowprayers",
            tags="tag1, tag2",
        )
        self.show.save()
        self.episode = milkman.deliver(Episode, show=self.show,
                                       title="Episode 1",tags="tag1, tag2")
        self.episode.save()
        self.enclosure = milkman.deliver(Enclosure, episode=self.episode)
        self.enclosure.save()
        self.app_url = reverse("podcasting_show_list")

    def test_podcast(self):
        self.assertEquals(self.show, self.enclosure.episode.show)
        self.assertEquals(self.show.get_absolute_url(),
                          self.app_url + "snowprayers/")
        self.assertEquals(self.episode.get_absolute_url(),
                          self.app_url + "snowprayers/episode/")

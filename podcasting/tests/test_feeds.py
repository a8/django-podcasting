# -*- coding: utf-8 -*-

"""UnitTests for all provided feeds
"""

try:
    from django.utils.datetime_safe import datetime
except ImportError:
    from datetime import datetime

import os
from xml.dom.minidom import parseString
from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from django.conf import settings

from milkman.dairy import milkman

from podcasting.models import Show, Episode, Enclosure


class AtomFeedTests(TestCase):
    def setUp(self):
        settings.ROOT_URLCONF = 'podcasting.tests.urls'
        self.show = milkman.deliver(
            Show, title="snowprayers",
            tags="tag1, tag2",
            main_category="Technology",
            original_image="media/show.png",
            published=datetime.now(),
            )
        self.show.save()
        self.episode = milkman.deliver(
            Episode,
            show=self.show,
            original_image="media/show.png",
            title="Episode 1",
            tags="tag1, tag2",
            published=datetime.now(),
        )
        self.episode.save()
        self.enclosure_mp3 = milkman.deliver(
            Enclosure,
            episode=self.episode,
            url="http://django-podcasting.org/podcasting/show/episode/media.mp3",
            mime="mp3",
        )
        self.enclosure_mp3.save()

    def test_enclosure_mp3(self):
        """Check for the one mp3 enclosure"""

        self.assertEqual(self.enclosure_mp3.episode, self.episode)
        response = self.client.get(reverse(
            'podcasts_show_feed_atom',
            kwargs={'show_slug': self.show.slug, 'mime_type': 'mp3'})
        )
        self.assertEquals(200, response.status_code)
        feed_dom = parseString(response.content)
        entries = feed_dom.getElementsByTagName('entry')
        self.assertGreaterEqual(len(entries), 1,
                                "Did not find any entries in Atom feed.")
        for entry in entries:
            mp3_enclosures = [l for l in entry.getElementsByTagName('link')\
                              if 'length' and 'type' and 'rel' in l.attributes.keys()\
                                 and l.getAttribute('type') == 'audio/mpeg'\
                                 and l.getAttribute('rel') == 'enclosure'
            ]
            self.assertEqual(len(mp3_enclosures), 1)
            for e in mp3_enclosures:
                self.assertTrue(isinstance(int(e.getAttribute('length')), int))

    def test_itunes_categroies(self):
        """Check if itunes:categories are set OK"""

        response = self.client.get(reverse(
            'podcasts_show_feed_atom',
            kwargs={'show_slug': self.show.slug, 'mime_type': 'mp3'})
        )
        self.assertEquals(200, response.status_code)
        feed_dom = parseString(response.content)
        category_tags = feed_dom.getElementsByTagName('itunes:category')
        self.assertGreaterEqual(len(category_tags), 1,
                                "Did not find any category tag in Atom feed.")
        for t in category_tags:
            self.assertTrue(t.hasAttributes())
            #Note, that will fire if sub categories are implemented
            self.assertFalse(t.hasChildNodes())
            self.assertEqual(1, len(t.attributes.keys()))
            self.assertTrue('text' in t.attributes.keys())
            self.assertEqual(self.show.main_category, t.getAttribute('text'))

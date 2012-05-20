# -*- coding: utf-8 -*-

"""UnitTests for all provided feeds
"""

try:
    from django.utils.datetime_safe import datetime
except ImportError:
    from datetime import datetime

import os
from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from django.conf import settings

from milkman.dairy import milkman

from podcasting.models import Show, Episode, Enclosure, MainCategory, SubCategory

class ShowTests(TestCase):

    def setUp(self):
        self.main_category = milkman.deliver(MainCategory)
        self.main_category.save()
        self.sub_category = milkman.deliver(SubCategory)
        self.sub_category.save()
        self.show_data = dict(
            title="snowprayers",
            tags="tag1, tag2",
            main_category=self.main_category,
            sub_categories=(self.sub_category,),
            original_image="media/show.png",
            published=datetime.now(),
            )
        self.show = milkman.deliver(
            Show,
            **self.show_data
            )
        self.show.save()

    def test_category(self):
        self.assertEqual(self.main_category,
                         self.show.main_category)
        #self.assertEqual('x', dir(self.show.sub_categories))
        self.assertTrue(self.sub_category in \
                         self.show.sub_categories.all())


# -*- coding: utf-8 -*-

"""UnitTests for all provided feeds
"""
import copy
import json

try:
    from django.utils.datetime_safe import datetime
except ImportError:
    from datetime import datetime

from django.test import TestCase, Client
from django.core.urlresolvers import reverse

from milkman.dairy import milkman

from podcasting.models import Show, Episode, Enclosure, MainCategory, SubCategory

class ShowTests(TestCase):
    fixtures = ["itunes_categories.json"]

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

    def test_admin_category_helper_view(self):
        """Test the data injected in the admin form."""
        response = self.client.get(reverse(
            "sub_categories_per_main_category",
            kwargs={'main_category_id': self.main_category.id, 'show_id': self.show.id})
        )
        self.assertEquals(200, response.status_code)

        # create new show obj with category data from fixture
        show_data = copy.deepcopy(self.show_data)
        main_category = MainCategory.objects.get(name="Technology")
        sub_category = SubCategory.objects.get(name="Software How-To",
                                               main_category=main_category)
        show_data['main_category'] = main_category
        show_data['sub_categories'] = [sub_category,]
        show = milkman.deliver(Show, **show_data)
        show.save()
        response = self.client.get(reverse(
            "sub_categories_per_main_category",
            kwargs={'main_category_id': main_category.id, 'show_id': show.id})
        )
        self.assertEquals(200, response.status_code)
        sub_categories = json.loads(response.content)
        # get sub_categories names as list
        sub_categories_per_main_category = SubCategory.objects.filter(
            main_category=main_category).values_list('name')
        sub_categories_per_main_category = [n[0] for n in sub_categories_per_main_category]

        for sub_category in sub_categories:
            # Check if possible sub category belongs to main category
            self.assertTrue(sub_category[1] in sub_categories_per_main_category)
            # test for already saved sub categories marked with True
            # used for html selected attr of multiple choice form in admin
            if sub_category[1] in [c.name for c in show.sub_categories.all()]:
                self.assertTrue(sub_category[2])
            else:
                self.assertFalse(sub_category[2])


#!/usr/bin/env python

# -*- coding: utf-8 -*-

"""
Create categories and sub categories as suggested by Apple in
http://www.apple.com/itunes/podcasts/specs.html

Note! For running django-podcasting you probably want to load
the fixture by

    python manage loadfixture path/to/podcasting/fixtures/categories.json

Once the data is loaded into the db it can be dumped to a file like that:
    python manage.py dumpdata podcasting.MainCategory podcasting.SubCategory > \
            categories.json
"""

__author__ = "Frank Becker <fb@alien8.de>"
__version__ = "$Revision: 0.0 $"
__date__ = "Fri Jun 22 22:40:05 CEST 2012"
__copyright__ = "Copyright (c) 2012 Frank Becker"
__license__ = "Python"

import os
import sys
from podcasting.models import MainCategory, SubCategory
from django.core.management import setup_environ

CATEGORIES = {
    "Arts": ["Design", "Fashion & Beauty", "Food", "Literature", "Performing Arts", "Visual Arts"],
    "Business": ["Business News", "Careers", "Investing", "Management & Marketing", "Shopping"],
    "Comedy": [],
    "Education": ["Education", "Education Technology", "Higher Education", "K-12", "Language Courses", "Training"],
    "Games & Hobbies": ["Automotive", "Aviation", "Hobbies", "Other Games", "Video Games"],
    "Government & Organizations": ["Local", "National", "Non-Profit", "Regional"],
    "Health": ["Alternative Health", "Fitness & Nutrition", "Self-Help", "Sexuality"],
    "Kids & Family": [],
    "Music": [],
    "News & Politics": [],
    "Religion & Spirituality": ["Buddhism", "Christianity", "Hinduism", "Islam", "Judaism", "Other", "Spirituality"],
    "Science & Medicine": ["Medicine", "Natural Sciences", "Social Sciences"],
    "Society & Culture": ["History", "Personal Journals", "Philosophy", "Places & Travel"],
    "Sports & Recreation": ["Amateur", "College & High School", "Outdoor", "Professional"],
    "Technology": ["Gadgets", "Tech News", "Podcasting", "Software How-To"],
    "TV & Film": [],
}

def load_categories():
    """load the categories into the database"""
    for main_category_name in CATEGORIES.keys():
        main_category = MainCategory(name=main_category_name)
        main_category.save()

        for sub_category_name in CATEGORIES[main_category_name]:
            sub_category = SubCategory(name=sub_category_name,
                                       main_category=main_category)
            sub_category.save()

def main():
    if MainCategory.objects.all():
        raise Exception("Found existing main categories.")
    load_categories()


if __name__ == '__main__':
    if not os.environ.has_key("DJANGO_SETTINGS_MODULE"):
        print ("You need to provide the environment variable "
               "DJANGO_SETTINGS_MODULE!")
        sys.exit(1)
    main()

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4 fileencoding=utf-8 :


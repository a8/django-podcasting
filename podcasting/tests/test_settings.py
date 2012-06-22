INSTALLED_APPS = (
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sites",
    "django_nose",
    "licenses",
    "podcasting",
    "podcasting.tests",
)

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
        }
    }


SITE_ID = 1

ROOT_URLCONF = "podcasting.tests.urls"

ADMIN_MEDIA_PREFIX = '/static/admin/'

TEST_RUNNER = "django_nose.NoseTestSuiteRunner"

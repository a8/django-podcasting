# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Show'
        db.create_table('podcasting_show', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('uuid', self.gf('django.db.models.fields.CharField')(unique=True, max_length=36, blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('published', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['sites.Site'])),
            ('ttl', self.gf('django.db.models.fields.PositiveIntegerField')(default=1440)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(related_name='podcast_shows', to=orm['auth.User'])),
            ('editor_email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('webmaster_email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('license', self.gf('licenses.fields.LicenseField')()),
            ('organization', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('link', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('enable_comments', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('author_text', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, blank=True)),
            ('subtitle', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')(max_length=4000)),
            ('original_image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('feedburner', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('explicit', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=1)),
            ('redirect', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('keywords', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('itunes', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('twitter_tweet_prefix', self.gf('django.db.models.fields.CharField')(max_length=80, blank=True)),
        ))
        db.send_create_signal('podcasting', ['Show'])

        # Adding model 'Episode'
        db.create_table('podcasting_episode', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('uuid', self.gf('django.db.models.fields.CharField')(unique=True, max_length=36, blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('published', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('show', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['podcasting.Show'])),
            ('enable_comments', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('author_text', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, blank=True)),
            ('subtitle', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')(max_length=4000)),
            ('tracklist', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('tweet_text', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('original_image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('hours', self.gf('django.db.models.fields.SmallIntegerField')(default=0, max_length=2)),
            ('minutes', self.gf('django.db.models.fields.SmallIntegerField')(default=0, max_length=2)),
            ('seconds', self.gf('django.db.models.fields.SmallIntegerField')(default=0, max_length=2)),
            ('keywords', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('explicit', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=1)),
            ('block', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('podcasting', ['Episode'])

        # Adding model 'Enclosure'
        db.create_table('podcasting_enclosure', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('episode', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['podcasting.Episode'])),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('size', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('mime', self.gf('django.db.models.fields.CharField')(default='mp3', max_length=4)),
            ('bitrate', self.gf('django.db.models.fields.CharField')(default='192', max_length=5)),
            ('sample', self.gf('django.db.models.fields.CharField')(default='44.1', max_length=5)),
            ('channel', self.gf('django.db.models.fields.CharField')(default=2, max_length=1)),
        ))
        db.send_create_signal('podcasting', ['Enclosure'])

        # Adding unique constraint on 'Enclosure', fields ['episode', 'mime']
        db.create_unique('podcasting_enclosure', ['episode_id', 'mime'])


    def backwards(self, orm):
        # Removing unique constraint on 'Enclosure', fields ['episode', 'mime']
        db.delete_unique('podcasting_enclosure', ['episode_id', 'mime'])

        # Deleting model 'Show'
        db.delete_table('podcasting_show')

        # Deleting model 'Episode'
        db.delete_table('podcasting_episode')

        # Deleting model 'Enclosure'
        db.delete_table('podcasting_enclosure')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'licenses.license': {
            'Meta': {'ordering': "('name',)", 'object_name': 'License'},
            'abbreviation': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'logo': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'organization': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'licenses'", 'null': 'True', 'to': "orm['licenses.Organization']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'licenses.organization': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Organization'},
            'abbreviation': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'podcasting.enclosure': {
            'Meta': {'ordering': "('episode', 'mime')", 'unique_together': "(('episode', 'mime'),)", 'object_name': 'Enclosure'},
            'bitrate': ('django.db.models.fields.CharField', [], {'default': "'192'", 'max_length': '5'}),
            'channel': ('django.db.models.fields.CharField', [], {'default': '2', 'max_length': '1'}),
            'episode': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['podcasting.Episode']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mime': ('django.db.models.fields.CharField', [], {'default': "'mp3'", 'max_length': '4'}),
            'sample': ('django.db.models.fields.CharField', [], {'default': "'44.1'", 'max_length': '5'}),
            'size': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'podcasting.episode': {
            'Meta': {'ordering': "('-published', 'slug')", 'object_name': 'Episode'},
            'author_text': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'block': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '4000'}),
            'enable_comments': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'explicit': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '1'}),
            'hours': ('django.db.models.fields.SmallIntegerField', [], {'default': '0', 'max_length': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'minutes': ('django.db.models.fields.SmallIntegerField', [], {'default': '0', 'max_length': '2'}),
            'original_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'published': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'seconds': ('django.db.models.fields.SmallIntegerField', [], {'default': '0', 'max_length': '2'}),
            'show': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['podcasting.Show']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'blank': 'True'}),
            'subtitle': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'tracklist': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'tweet_text': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '36', 'blank': 'True'})
        },
        'podcasting.show': {
            'Meta': {'ordering': "('organization', 'slug')", 'object_name': 'Show'},
            'author_text': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '4000'}),
            'editor_email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'enable_comments': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'explicit': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '1'}),
            'feedburner': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'itunes': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'license': ('licenses.fields.LicenseField', [], {}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'organization': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'original_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'podcast_shows'", 'to': "orm['auth.User']"}),
            'published': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'redirect': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': "orm['sites.Site']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'blank': 'True'}),
            'subtitle': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'ttl': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1440'}),
            'twitter_tweet_prefix': ('django.db.models.fields.CharField', [], {'max_length': '80', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '36', 'blank': 'True'}),
            'webmaster_email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'})
        },
        'sites.site': {
            'Meta': {'ordering': "('domain',)", 'object_name': 'Site', 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'taggit.tag': {
            'Meta': {'object_name': 'Tag'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'})
        },
        'taggit.taggeditem': {
            'Meta': {'object_name': 'TaggedItem'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'taggit_taggeditem_tagged_items'", 'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'taggit_taggeditem_items'", 'to': "orm['taggit.Tag']"})
        }
    }

    complete_apps = ['podcasting']
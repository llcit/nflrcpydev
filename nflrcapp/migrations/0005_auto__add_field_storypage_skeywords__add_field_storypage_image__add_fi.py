# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'StoryPage.skeywords'
        db.add_column(u'nflrcapp_storypage', 'skeywords',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'StoryPage.image'
        db.add_column(u'nflrcapp_storypage', 'image',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100L, blank=True),
                      keep_default=False)

        # Adding field 'StoryPage.featured'
        db.add_column(u'nflrcapp_storypage', 'featured',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'StoryPage.headline'
        db.add_column(u'nflrcapp_storypage', 'headline',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'StoryPage.skeywords'
        db.delete_column(u'nflrcapp_storypage', 'skeywords')

        # Deleting field 'StoryPage.image'
        db.delete_column(u'nflrcapp_storypage', 'image')

        # Deleting field 'StoryPage.featured'
        db.delete_column(u'nflrcapp_storypage', 'featured')

        # Deleting field 'StoryPage.headline'
        db.delete_column(u'nflrcapp_storypage', 'headline')


    models = {
        u'nflrcapp.contact': {
            'Meta': {'object_name': 'Contact'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '128L', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '20L', 'blank': 'True'}),
            'current_project': ('django.db.models.fields.CharField', [], {'max_length': '255L', 'null': 'True', 'blank': 'True'}),
            'department': ('django.db.models.fields.CharField', [], {'max_length': '256L', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '40L', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50L'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'blank': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '20L', 'blank': 'True'}),
            'listing_rank': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'nflrc_staff': ('django.db.models.fields.BooleanField', [], {}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '40L', 'blank': 'True'}),
            'role': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '15L', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50L', 'blank': 'True'}),
            'university': ('django.db.models.fields.CharField', [], {'max_length': '60L', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'zipcode': ('django.db.models.fields.CharField', [], {'max_length': '15L', 'blank': 'True'})
        },
        u'nflrcapp.personproject': {
            'Meta': {'object_name': 'PersonProject'},
            'contact_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['nflrcapp.Contact']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'project_number': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['nflrcapp.Project']"}),
            'status': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'nflrcapp.personpublication': {
            'Meta': {'object_name': 'PersonPublication'},
            'contact_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['nflrcapp.Contact']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'publication_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['nflrcapp.Publication']"})
        },
        u'nflrcapp.prodev': {
            'Meta': {'object_name': 'Prodev'},
            'date': ('django.db.models.fields.CharField', [], {'max_length': '50L', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'director': ('django.db.models.fields.CharField', [], {'max_length': '200L'}),
            'facilitator': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'headline': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'blank': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'blank': 'True'}),
            'pdtype': ('django.db.models.fields.CharField', [], {'max_length': '30L', 'blank': 'True'}),
            'related_publication': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'skeywords': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200L', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'nflrcapp.project': {
            'Meta': {'object_name': 'Project'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'director': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'grant_cycle': ('django.db.models.fields.CharField', [], {'max_length': '50L', 'blank': 'True'}),
            'headline': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'blank': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '80L', 'blank': 'True'}),
            'project_number': ('django.db.models.fields.CharField', [], {'max_length': '10L'}),
            'skeywords': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '30L', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '150L', 'blank': 'True'})
        },
        u'nflrcapp.publication': {
            'Meta': {'object_name': 'Publication'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'blank': 'True'}),
            'category': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'headline': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'blank': 'True'}),
            'isbn': ('django.db.models.fields.CharField', [], {'max_length': '20L', 'null': 'True', 'blank': 'True'}),
            'item_number': ('django.db.models.fields.CharField', [], {'max_length': '10L', 'blank': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '255L', 'blank': 'True'}),
            'order_from': ('django.db.models.fields.CharField', [], {'max_length': '10L', 'blank': 'True'}),
            'price': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'size': ('django.db.models.fields.CharField', [], {'max_length': '40L', 'blank': 'True'}),
            'skeywords': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200L', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '250L', 'blank': 'True'}),
            'year': ('django.db.models.fields.CharField', [], {'max_length': '12L', 'blank': 'True'})
        },
        u'nflrcapp.resource': {
            'Meta': {'object_name': 'Resource'},
            'contact_email': ('django.db.models.fields.CharField', [], {'max_length': '60L', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.CharField', [], {'max_length': '50L', 'blank': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '200L', 'blank': 'True'}),
            'language_group': ('django.db.models.fields.CharField', [], {'max_length': '60L', 'blank': 'True'}),
            'resource_number': ('django.db.models.fields.IntegerField', [], {}),
            'site_type': ('django.db.models.fields.CharField', [], {'max_length': '60L', 'blank': 'True'}),
            'site_type1': ('django.db.models.fields.CharField', [], {'max_length': '60L', 'blank': 'True'}),
            'site_type2': ('django.db.models.fields.CharField', [], {'max_length': '60L', 'blank': 'True'}),
            'site_type3': ('django.db.models.fields.CharField', [], {'max_length': '60L', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '150L', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        u'nflrcapp.software': {
            'Meta': {'object_name': 'Software'},
            'age': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'blank': 'True'}),
            'content': ('django.db.models.fields.CharField', [], {'max_length': '1000L', 'blank': 'True'}),
            'distributor': ('django.db.models.fields.CharField', [], {'max_length': '600L', 'blank': 'True'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'blank': 'True'}),
            'featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'format': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'blank': 'True'}),
            'geneemail': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'hardwares': ('django.db.models.fields.CharField', [], {'max_length': '1500L', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'infoemail': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'languages': ('django.db.models.fields.CharField', [], {'max_length': '100L'}),
            'levels': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'blank': 'True'}),
            'platforms': ('django.db.models.fields.CharField', [], {'max_length': '300L', 'blank': 'True'}),
            'price': ('django.db.models.fields.CharField', [], {'max_length': '200L', 'blank': 'True'}),
            'review': ('django.db.models.fields.CharField', [], {'max_length': '1000L', 'blank': 'True'}),
            'saleemail': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'skills': ('django.db.models.fields.CharField', [], {'max_length': '200L', 'blank': 'True'}),
            'telephone': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200L'}),
            'www': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        u'nflrcapp.storypage': {
            'Meta': {'object_name': 'StoryPage'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'headline': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'blank': 'True'}),
            'skeywords': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        }
    }

    complete_apps = ['nflrcapp']
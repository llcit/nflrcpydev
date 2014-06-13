# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Project.image'
        db.alter_column(u'nflrcapp_project', 'image', self.gf('django.db.models.fields.CharField')(max_length=100L))
        # Adding field 'Publication.is_oer'
        db.add_column(u'nflrcapp_publication', 'is_oer',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Publication.ext_url'
        db.add_column(u'nflrcapp_publication', 'ext_url',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=250L, blank=True),
                      keep_default=False)

        # Adding field 'Publication.oclc_url'
        db.add_column(u'nflrcapp_publication', 'oclc_url',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=250L, blank=True),
                      keep_default=False)

        # Adding field 'Publication.hidden'
        db.add_column(u'nflrcapp_publication', 'hidden',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


        # Changing field 'StoryPage.thumbnail_desc'
        db.alter_column(u'nflrcapp_storypage', 'thumbnail_desc', self.gf('django.db.models.fields.CharField')(max_length=160, null=True))

    def backwards(self, orm):

        # Changing field 'Project.image'
        db.alter_column(u'nflrcapp_project', 'image', self.gf('django.db.models.fields.CharField')(max_length=100L, null=True))
        # Deleting field 'Publication.is_oer'
        db.delete_column(u'nflrcapp_publication', 'is_oer')

        # Deleting field 'Publication.ext_url'
        db.delete_column(u'nflrcapp_publication', 'ext_url')

        # Deleting field 'Publication.oclc_url'
        db.delete_column(u'nflrcapp_publication', 'oclc_url')

        # Deleting field 'Publication.hidden'
        db.delete_column(u'nflrcapp_publication', 'hidden')


        # Changing field 'StoryPage.thumbnail_desc'
        db.alter_column(u'nflrcapp_storypage', 'thumbnail_desc', self.gf('django.db.models.fields.CharField')(default='more...', max_length=160))

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
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
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
            'headline_tag': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '512', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.CharField', [], {'default': "u'icon.png'", 'max_length': '100L', 'blank': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'blank': 'True'}),
            'pdtype': ('django.db.models.fields.CharField', [], {'max_length': '30L', 'blank': 'True'}),
            'related_publication': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'skeywords': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'thumbnail_desc': ('django.db.models.fields.CharField', [], {'default': "u'more...'", 'max_length': '160', 'null': 'True', 'blank': 'True'}),
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
            'headline_tag': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '512', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.CharField', [], {'default': "u'icon.png'", 'max_length': '100L', 'blank': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '80L', 'blank': 'True'}),
            'project_number': ('django.db.models.fields.CharField', [], {'max_length': '10L'}),
            'skeywords': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '30L', 'blank': 'True'}),
            'thumbnail_desc': ('django.db.models.fields.CharField', [], {'default': "u'more...'", 'max_length': '160', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '150L', 'blank': 'True'})
        },
        u'nflrcapp.publication': {
            'Meta': {'ordering': "[u'-year', u'item_number']", 'object_name': 'Publication'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'blank': 'True'}),
            'category': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'ext_url': ('django.db.models.fields.CharField', [], {'max_length': '250L', 'blank': 'True'}),
            'featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'headline': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'headline_tag': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'hidden': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.CharField', [], {'default': "u'icon.png'", 'max_length': '100L', 'blank': 'True'}),
            'is_oer': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'isbn': ('django.db.models.fields.CharField', [], {'max_length': '20L', 'null': 'True', 'blank': 'True'}),
            'item_number': ('django.db.models.fields.CharField', [], {'max_length': '10L', 'blank': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '255L', 'blank': 'True'}),
            'oclc_url': ('django.db.models.fields.CharField', [], {'max_length': '250L', 'blank': 'True'}),
            'order_from': ('django.db.models.fields.CharField', [], {'max_length': '10L', 'blank': 'True'}),
            'price': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'size': ('django.db.models.fields.CharField', [], {'max_length': '40L', 'blank': 'True'}),
            'skeywords': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'thumbnail_desc': ('django.db.models.fields.CharField', [], {'default': "u'more...'", 'max_length': '160', 'null': 'True', 'blank': 'True'}),
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
            'headline_tag': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '512', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.CharField', [], {'default': "u'icon.png'", 'max_length': '100L', 'blank': 'True'}),
            'skeywords': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'thumbnail_desc': ('django.db.models.fields.CharField', [], {'default': "u'more...'", 'max_length': '160', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        }
    }

    complete_apps = ['nflrcapp']
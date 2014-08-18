# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ItemTag'
        db.create_table(u'nflrcapp_itemtag', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tag', self.gf('django.db.models.fields.CharField')(max_length=140)),
        ))
        db.send_create_signal(u'nflrcapp', ['ItemTag'])

        # Adding model 'TaggedItem'
        db.create_table(u'nflrcapp_taggeditem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tag', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['nflrcapp.ItemTag'])),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('object_id', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal(u'nflrcapp', ['TaggedItem'])


    def backwards(self, orm):
        # Deleting model 'ItemTag'
        db.delete_table(u'nflrcapp_itemtag')

        # Deleting model 'TaggedItem'
        db.delete_table(u'nflrcapp_taggeditem')


    models = {
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'nflrcapp.contact': {
            'Meta': {'object_name': 'Contact'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '128L', 'blank': 'True'}),
            'bio': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '20L', 'blank': 'True'}),
            'current_project': ('django.db.models.fields.CharField', [], {'max_length': '255L', 'null': 'True', 'blank': 'True'}),
            'department': ('django.db.models.fields.CharField', [], {'max_length': '256L', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '40L', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50L'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'blank': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '20L'}),
            'listing_rank': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'nflrc_staff': ('django.db.models.fields.BooleanField', [], {}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '40L', 'blank': 'True'}),
            'role': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'staff_role': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['nflrcapp.ContactRole']", 'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '15L', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'university': ('django.db.models.fields.CharField', [], {'max_length': '60L', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'zipcode': ('django.db.models.fields.CharField', [], {'max_length': '15L', 'blank': 'True'})
        },
        u'nflrcapp.contactrole': {
            'Meta': {'object_name': 'ContactRole'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'list_rank': ('django.db.models.fields.IntegerField', [], {'default': '1000', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'nflrcapp.itemtag': {
            'Meta': {'object_name': 'ItemTag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tag': ('django.db.models.fields.CharField', [], {'max_length': '140'})
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
            'featured_rank': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
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
            'featured_rank': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
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
            'author': ('django.db.models.fields.CharField', [], {'max_length': '100L'}),
            'category': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'ext_url': ('django.db.models.fields.CharField', [], {'max_length': '250L', 'blank': 'True'}),
            'featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'featured_rank': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'headline': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'headline_tag': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'hidden': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.CharField', [], {'default': "u'icon.png'", 'max_length': '100L'}),
            'is_oer': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'isbn': ('django.db.models.fields.CharField', [], {'max_length': '20L', 'null': 'True', 'blank': 'True'}),
            'item_number': ('django.db.models.fields.CharField', [], {'max_length': '10L'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '255L', 'blank': 'True'}),
            'oclc_url': ('django.db.models.fields.CharField', [], {'max_length': '250L', 'blank': 'True'}),
            'order_from': ('django.db.models.fields.CharField', [], {'max_length': '250L', 'blank': 'True'}),
            'price': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'size': ('django.db.models.fields.CharField', [], {'max_length': '40L', 'blank': 'True'}),
            'skeywords': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'thumbnail_desc': ('django.db.models.fields.CharField', [], {'default': "u'more...'", 'max_length': '160', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200L'}),
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
            'featured_rank': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'headline': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'headline_tag': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '512', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.CharField', [], {'default': "u'icon.png'", 'max_length': '100L', 'blank': 'True'}),
            'skeywords': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'thumbnail_desc': ('django.db.models.fields.CharField', [], {'default': "u'more...'", 'max_length': '160', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'nflrcapp.taggeditem': {
            'Meta': {'object_name': 'TaggedItem'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['nflrcapp.ItemTag']"})
        }
    }

    complete_apps = ['nflrcapp']
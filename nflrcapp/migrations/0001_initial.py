# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Contact'
        db.create_table(u'nflrcapp_contact', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=50L)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50L, blank=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=20L, blank=True)),
            ('department', self.gf('django.db.models.fields.CharField')(max_length=256L, blank=True)),
            ('university', self.gf('django.db.models.fields.CharField')(max_length=60L, blank=True)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=128L, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=20L, blank=True)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=15L, blank=True)),
            ('zipcode', self.gf('django.db.models.fields.CharField')(max_length=15L, blank=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=40L, blank=True)),
            ('fax', self.gf('django.db.models.fields.CharField')(max_length=40L, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('current_project', self.gf('django.db.models.fields.CharField')(max_length=255L, null=True, blank=True)),
            ('nflrc_staff', self.gf('django.db.models.fields.BooleanField')()),
            ('listing_rank', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'nflrcapp', ['Contact'])

        # Adding model 'Prodev'
        db.create_table(u'nflrcapp_prodev', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200L, blank=True)),
            ('language', self.gf('django.db.models.fields.CharField')(max_length=100L, blank=True)),
            ('date', self.gf('django.db.models.fields.CharField')(max_length=50L, blank=True)),
            ('pdtype', self.gf('django.db.models.fields.CharField')(max_length=30L, blank=True)),
            ('director', self.gf('django.db.models.fields.CharField')(max_length=200L)),
            ('facilitator', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('related_publication', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('skeywords', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('featured', self.gf('django.db.models.fields.BooleanField')()),
            ('headline', self.gf('django.db.models.fields.BooleanField')()),
        ))
        db.send_create_signal(u'nflrcapp', ['Prodev'])

        # Adding model 'Project'
        db.create_table(u'nflrcapp_project', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('project_number', self.gf('django.db.models.fields.CharField')(max_length=10L)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=150L, blank=True)),
            ('language', self.gf('django.db.models.fields.CharField')(max_length=80L, blank=True)),
            ('grant_cycle', self.gf('django.db.models.fields.CharField')(max_length=50L, blank=True)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=30L, blank=True)),
            ('director', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('skeywords', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('featured', self.gf('django.db.models.fields.BooleanField')()),
            ('headline', self.gf('django.db.models.fields.BooleanField')()),
        ))
        db.send_create_signal(u'nflrcapp', ['Project'])

        # Adding model 'PersonProject'
        db.create_table(u'nflrcapp_personproject', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('contact_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['nflrcapp.Contact'])),
            ('project_number', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['nflrcapp.Project'])),
            ('status', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'nflrcapp', ['PersonProject'])

        # Adding model 'Publication'
        db.create_table(u'nflrcapp_publication', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('item_number', self.gf('django.db.models.fields.CharField')(max_length=10L, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200L, blank=True)),
            ('language', self.gf('django.db.models.fields.CharField')(max_length=255L, blank=True)),
            ('category', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('author', self.gf('django.db.models.fields.CharField')(max_length=100L, blank=True)),
            ('year', self.gf('django.db.models.fields.CharField')(max_length=12L, blank=True)),
            ('price', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('size', self.gf('django.db.models.fields.CharField')(max_length=40L, blank=True)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=250L, blank=True)),
            ('order_from', self.gf('django.db.models.fields.CharField')(max_length=10L, blank=True)),
            ('skeywords', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('image', self.gf('django.db.models.fields.CharField')(max_length=100L, blank=True)),
            ('isbn', self.gf('django.db.models.fields.CharField')(max_length=20L, blank=True)),
            ('featured', self.gf('django.db.models.fields.BooleanField')()),
            ('headline', self.gf('django.db.models.fields.BooleanField')()),
        ))
        db.send_create_signal(u'nflrcapp', ['Publication'])

        # Adding model 'PersonPublication'
        db.create_table(u'nflrcapp_personpublication', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('contact_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['nflrcapp.Contact'])),
            ('publication_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['nflrcapp.Publication'])),
        ))
        db.send_create_signal(u'nflrcapp', ['PersonPublication'])

        # Adding model 'Resource'
        db.create_table(u'nflrcapp_resource', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('resource_number', self.gf('django.db.models.fields.IntegerField')()),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=150L, blank=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('site_type', self.gf('django.db.models.fields.CharField')(max_length=60L, blank=True)),
            ('language', self.gf('django.db.models.fields.CharField')(max_length=200L, blank=True)),
            ('language_group', self.gf('django.db.models.fields.CharField')(max_length=60L, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('status', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('contact_email', self.gf('django.db.models.fields.CharField')(max_length=60L, null=True, blank=True)),
            ('site_type1', self.gf('django.db.models.fields.CharField')(max_length=60L, blank=True)),
            ('site_type2', self.gf('django.db.models.fields.CharField')(max_length=60L, blank=True)),
            ('site_type3', self.gf('django.db.models.fields.CharField')(max_length=60L, blank=True)),
            ('image', self.gf('django.db.models.fields.CharField')(max_length=50L, blank=True)),
            ('featured', self.gf('django.db.models.fields.BooleanField')()),
        ))
        db.send_create_signal(u'nflrcapp', ['Resource'])

        # Adding model 'Software'
        db.create_table(u'nflrcapp_software', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200L)),
            ('content', self.gf('django.db.models.fields.CharField')(max_length=1000L, blank=True)),
            ('languages', self.gf('django.db.models.fields.CharField')(max_length=100L)),
            ('skills', self.gf('django.db.models.fields.CharField')(max_length=200L, blank=True)),
            ('levels', self.gf('django.db.models.fields.CharField')(max_length=100L, blank=True)),
            ('age', self.gf('django.db.models.fields.CharField')(max_length=100L, blank=True)),
            ('format', self.gf('django.db.models.fields.CharField')(max_length=100L, blank=True)),
            ('platforms', self.gf('django.db.models.fields.CharField')(max_length=300L, blank=True)),
            ('hardwares', self.gf('django.db.models.fields.CharField')(max_length=1500L, blank=True)),
            ('distributor', self.gf('django.db.models.fields.CharField')(max_length=600L, blank=True)),
            ('telephone', self.gf('django.db.models.fields.CharField')(max_length=100L, blank=True)),
            ('fax', self.gf('django.db.models.fields.CharField')(max_length=100L, blank=True)),
            ('infoemail', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('saleemail', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('geneemail', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('www', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('price', self.gf('django.db.models.fields.CharField')(max_length=200L, blank=True)),
            ('review', self.gf('django.db.models.fields.CharField')(max_length=1000L, blank=True)),
            ('featured', self.gf('django.db.models.fields.BooleanField')()),
        ))
        db.send_create_signal(u'nflrcapp', ['Software'])


    def backwards(self, orm):
        # Deleting model 'Contact'
        db.delete_table(u'nflrcapp_contact')

        # Deleting model 'Prodev'
        db.delete_table(u'nflrcapp_prodev')

        # Deleting model 'Project'
        db.delete_table(u'nflrcapp_project')

        # Deleting model 'PersonProject'
        db.delete_table(u'nflrcapp_personproject')

        # Deleting model 'Publication'
        db.delete_table(u'nflrcapp_publication')

        # Deleting model 'PersonPublication'
        db.delete_table(u'nflrcapp_personpublication')

        # Deleting model 'Resource'
        db.delete_table(u'nflrcapp_resource')

        # Deleting model 'Software'
        db.delete_table(u'nflrcapp_software')


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
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '20L', 'blank': 'True'}),
            'listing_rank': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'nflrc_staff': ('django.db.models.fields.BooleanField', [], {}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '40L', 'blank': 'True'}),
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
            'featured': ('django.db.models.fields.BooleanField', [], {}),
            'headline': ('django.db.models.fields.BooleanField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
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
            'featured': ('django.db.models.fields.BooleanField', [], {}),
            'grant_cycle': ('django.db.models.fields.CharField', [], {'max_length': '50L', 'blank': 'True'}),
            'headline': ('django.db.models.fields.BooleanField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
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
            'featured': ('django.db.models.fields.BooleanField', [], {}),
            'headline': ('django.db.models.fields.BooleanField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'blank': 'True'}),
            'isbn': ('django.db.models.fields.CharField', [], {'max_length': '20L', 'blank': 'True'}),
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
            'featured': ('django.db.models.fields.BooleanField', [], {}),
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
            'featured': ('django.db.models.fields.BooleanField', [], {}),
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
        }
    }

    complete_apps = ['nflrcapp']
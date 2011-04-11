# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Adding model 'Host'
        db.create_table('hostfilter_host', (
            ('hostname', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('allowed_pattern', self.gf('django.db.models.fields.TextField')()),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('hostfilter', ['Host'])
    
    
    def backwards(self, orm):
        
        # Deleting model 'Host'
        db.delete_table('hostfilter_host')
    
    
    models = {
        'hostfilter.host': {
            'Meta': {'object_name': 'Host'},
            'allowed_pattern': ('django.db.models.fields.TextField', [], {}),
            'hostname': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }
    
    complete_apps = ['hostfilter']

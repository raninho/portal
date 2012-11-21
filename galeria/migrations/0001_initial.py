# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Imagem'
        db.create_table('Imagens', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('descricao', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('imagem', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal('galeria', ['Imagem'])


    def backwards(self, orm):
        # Deleting model 'Imagem'
        db.delete_table('Imagens')


    models = {
        'galeria.imagem': {
            'Meta': {'object_name': 'Imagem', 'db_table': "'Imagens'"},
            'descricao': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagem': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['galeria']
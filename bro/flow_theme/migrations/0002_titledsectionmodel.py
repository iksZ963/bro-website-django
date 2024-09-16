# Generated by Django 5.0.2 on 2024-09-16 11:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0037_alter_cmsplugin_id_alter_globalpagepermission_id_and_more'),
        ('flow_theme', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TitledSectionModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='%(app_label)s_%(class)s', serialize=False, to='cms.cmsplugin')),
                ('section_title', models.CharField(blank=True, default='', max_length=127)),
            ],
            bases=('cms.cmsplugin',),
        ),
    ]

# Generated by Django 5.0.8 on 2024-09-15 10:16

import cms.models.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bro_frontend', '0004_accordionitemmodel'),
        ('cms', '0035_auto_20230822_2208_squashed_0036_auto_20240311_1028'),
    ]

    operations = [
        migrations.CreateModel(
            name='LinkModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='%(app_label)s_%(class)s', serialize=False, to='cms.cmsplugin')),
                ('type', models.CharField(choices=[('', 'Default'), ('btn', 'Button'), ('link', 'Link')], default='', max_length=63)),
                ('variant', models.CharField(choices=[('', 'Default'), ('btn-primary', 'Primary Button'), ('btn-secondary', 'Secondary Button'), ('btn-accent', 'Accent Button'), ('btn-info', 'Info Button'), ('btn-success', 'Success Button'), ('btn-warning', 'Warning Button'), ('btn-error', 'Error Button'), ('btn-link', 'Link Button')], default='', max_length=63)),
                ('link', cms.models.fields.PageField(null=True, on_delete=django.db.models.deletion.CASCADE, to='cms.page')),
            ],
            bases=('cms.cmsplugin',),
        ),
    ]

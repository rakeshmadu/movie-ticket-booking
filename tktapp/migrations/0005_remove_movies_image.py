# Generated by Django 2.2.3 on 2019-08-09 06:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tktapp', '0004_auto_20190809_0650'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movies',
            name='image',
        ),
    ]

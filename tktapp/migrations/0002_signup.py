# Generated by Django 2.2.3 on 2019-08-08 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tktapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Signup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('mobileno', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
    ]

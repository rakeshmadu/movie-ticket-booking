# Generated by Django 2.2.3 on 2019-08-09 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tktapp', '0006_auto_20190809_0903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='time',
            field=models.CharField(choices=[('11:45 am', '11:45 am'), ('2:45 pm', '2:45 pm'), ('6:45 pm', '6:45 pm'), ('9:45 pm', '9:45 pm')], max_length=30),
        ),
    ]

# Generated by Django 2.2.3 on 2019-08-09 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tktapp', '0007_auto_20190809_0959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='price',
            field=models.CharField(choices=[('₹70', '₹70'), ('₹100', '₹100'), ('₹150', '₹150')], max_length=30),
        ),
    ]

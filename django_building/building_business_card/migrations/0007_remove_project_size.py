# Generated by Django 3.2.9 on 2021-12-19 11:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('building_business_card', '0006_auto_20211219_1119'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='size',
        ),
    ]

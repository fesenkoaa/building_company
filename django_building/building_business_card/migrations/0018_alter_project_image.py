# Generated by Django 3.2.9 on 2022-02-13 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('building_business_card', '0017_auto_20220213_1855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]
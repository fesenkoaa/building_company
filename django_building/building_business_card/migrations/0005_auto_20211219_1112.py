# Generated by Django 3.2.9 on 2021-12-19 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('building_business_card', '0004_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='end',
            field=models.IntegerField(verbose_name='Year of end'),
        ),
        migrations.AlterField(
            model_name='project',
            name='start',
            field=models.IntegerField(verbose_name='Year of start'),
        ),
    ]

# Generated by Django 3.2.9 on 2022-01-17 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('building_business_card', '0011_auto_20220114_1448'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(unique=True, upload_to='', verbose_name='image')),
            ],
        ),
    ]
# Generated by Django 3.2.9 on 2022-02-12 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('building_business_card', '0015_auto_20220201_1150'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wallpaper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.AlterField(
            model_name='newemployee',
            name='location',
            field=models.CharField(max_length=100, verbose_name='город, в котором сейчас находитесь'),
        ),
    ]

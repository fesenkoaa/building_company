# Generated by Django 3.2.9 on 2022-04-09 09:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('building_eng', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ennewemployee',
            name='first_name',
            field=models.CharField(max_length=100, verbose_name='first name'),
        ),
        migrations.AlterField(
            model_name='ennewemployee',
            name='last_name',
            field=models.CharField(max_length=100, verbose_name='last name'),
        ),
        migrations.AlterField(
            model_name='ennewemployee',
            name='location',
            field=models.CharField(max_length=100, verbose_name='current city'),
        ),
        migrations.AlterField(
            model_name='ennewemployee',
            name='phone',
            field=models.BigIntegerField(verbose_name='phone'),
        ),
        migrations.AlterField(
            model_name='ennewemployee',
            name='position',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='building_eng.envacancy', verbose_name='Available vacancies'),
        ),
        migrations.AlterField(
            model_name='ennewemployee',
            name='year',
            field=models.IntegerField(max_length=10, verbose_name='year of birthday'),
        ),
    ]
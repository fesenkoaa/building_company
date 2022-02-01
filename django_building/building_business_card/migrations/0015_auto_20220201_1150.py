# Generated by Django 3.2.9 on 2022-02-01 11:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('building_business_card', '0014_auto_20220201_1038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.BigIntegerField(verbose_name='Phone'),
        ),
        migrations.AlterField(
            model_name='newemployee',
            name='position',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='building_business_card.vacancy', verbose_name='Доступные должности'),
        ),
    ]
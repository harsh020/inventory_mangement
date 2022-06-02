# Generated by Django 3.2 on 2022-06-02 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='is_active'),
        ),
        migrations.AlterField(
            model_name='address',
            name='is_deleted',
            field=models.BooleanField(default=False, verbose_name='is_deleted'),
        ),
    ]
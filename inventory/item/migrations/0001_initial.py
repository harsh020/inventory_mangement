# Generated by Django 3.2 on 2022-06-01 17:26

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('warehouse', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('is_active', models.BooleanField(blank=True, default=True, null=True, verbose_name='is_active')),
                ('is_deleted', models.BooleanField(blank=True, default=False, null=True, verbose_name='is_deleted')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Name')),
                ('slug', models.SlugField(blank=True, max_length=120, null=True, verbose_name='Slug')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('is_active', models.BooleanField(blank=True, default=True, null=True, verbose_name='is_active')),
                ('is_deleted', models.BooleanField(blank=True, default=False, null=True, verbose_name='is_deleted')),
                ('name', models.CharField(blank=True, max_length=200, null=True, verbose_name='Name')),
                ('image', models.ImageField(blank=True, default='placeholder.png', null=True, upload_to='', verbose_name='Image')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('brand', models.CharField(blank=True, max_length=100, null=True, verbose_name='Brand')),
                ('price', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True, verbose_name='Price')),
                ('count_in_stock', models.IntegerField(blank=True, default=0, null=True, verbose_name='Count')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='category_items', to='item.category')),
                ('warehouse', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='warehouse_items', to='warehouse.warehouse')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

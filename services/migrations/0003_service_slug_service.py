# Generated by Django 3.2.9 on 2021-11-08 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_rename_serice_title_service_service_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='slug_service',
            field=models.SlugField(default='', max_length=200, unique=True),
            preserve_default=False,
        ),
    ]
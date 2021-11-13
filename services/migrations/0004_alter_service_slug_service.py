# Generated by Django 3.2.9 on 2021-11-13 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_service_slug_service'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='slug_service',
            field=models.SlugField(max_length=200, null=True, unique=True),
        ),
    ]
# Generated by Django 4.2.2 on 2023-07-21 16:24

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attraction', '0003_rename_imageattraction_image_attraction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attraction',
            name='descript',
            field=ckeditor.fields.RichTextField(),
        ),
    ]

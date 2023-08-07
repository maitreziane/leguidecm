# Generated by Django 4.2.2 on 2023-06-23 14:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category_attraction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_attr', models.CharField(max_length=255)),
                ('slug_type', models.SlugField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Attraction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('ville', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, upload_to='uploads/attraction')),
                ('descript', models.TextField(blank=True, null=True)),
                ('category', models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='attraction.category_attraction')),
            ],
        ),
    ]
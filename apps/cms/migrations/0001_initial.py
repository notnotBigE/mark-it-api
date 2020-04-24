# Generated by Django 3.0.5 on 2020-04-24 21:46

import apps.cms.fields
import datetime
from django.db import migrations, models
import django.db.models.deletion
import djrichtextfield.models
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meta_title', models.CharField(blank=True, max_length=80, null=True, verbose_name='<meta> title')),
                ('meta_description', models.CharField(blank=True, max_length=160, null=True, verbose_name='<meta> description')),
                ('og_title', models.CharField(blank=True, max_length=80, null=True, verbose_name=' og:title')),
                ('og_type', models.CharField(choices=[('video.other', 'Video'), ('video.movie', 'Movie'), ('video.tv_show', 'TV Show'), ('article', 'Article'), ('book', 'Book'), ('profile', 'Profile'), ('website', 'Website')], default='website', max_length=30, verbose_name=' og:type')),
                ('og_description', models.CharField(blank=True, max_length=200, null=True, verbose_name=' og:description')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=140, unique=True)),
                ('sub_title', models.CharField(max_length=255)),
                ('layout', models.CharField(choices=[('simple', 'Simple'), ('sectioned', 'Sectioned')], default='simple', max_length=30)),
                ('body', djrichtextfield.models.RichTextField(blank=True, null=True)),
                ('sidebar', djrichtextfield.models.RichTextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='cms.Page')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=140, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='section_images')),
                ('body', djrichtextfield.models.RichTextField(null=True)),
                ('sort_order', models.PositiveIntegerField(default=0)),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms.Page')),
            ],
            options={
                'ordering': ['sort_order'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=140, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('published', models.BooleanField(default=False)),
                ('published_on', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('feature_image', models.ImageField(blank=True, null=True, upload_to='feature_images')),
                ('feature_color', apps.cms.fields.ColorField(blank=True, default='#ffffff', max_length=7, null=True, verbose_name='Feature Color')),
                ('body', djrichtextfield.models.RichTextField(blank=True, null=True)),
                ('tags', models.ManyToManyField(related_name='tags', to='cms.Tag')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

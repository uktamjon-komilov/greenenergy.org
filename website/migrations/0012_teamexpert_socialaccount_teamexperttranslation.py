# Generated by Django 4.0.2 on 2022-02-24 22:26

from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms
import parler.fields
import parler.models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0011_choose_choosetranslation'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamExpert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField()),
                ('image', django_resized.forms.ResizedImageField(crop=['middle', 'center'], force_format=None, keep_meta=True, quality=100, size=[367, 400], upload_to='images/')),
            ],
            options={
                'abstract': False,
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='SocialAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.TextField()),
                ('icon', models.FileField(blank=True, null=True, upload_to='')),
                ('icon_text', models.CharField(blank=True, max_length=255, null=True)),
                ('team_expert', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='website.teamexpert')),
            ],
        ),
        migrations.CreateModel(
            name='TeamExpertTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('job', models.CharField(max_length=255)),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='website.teamexpert')),
            ],
            options={
                'verbose_name': 'team expert Translation',
                'db_table': 'website_teamexpert_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
    ]

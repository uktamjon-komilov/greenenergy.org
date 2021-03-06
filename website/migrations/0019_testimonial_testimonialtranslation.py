# Generated by Django 4.0.2 on 2022-02-25 12:25

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms
import parler.fields
import parler.models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0018_alter_processitem_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=30)),
                ('image', django_resized.forms.ResizedImageField(crop=['middle', 'center'], force_format=None, keep_meta=True, quality=100, size=[100, 100], upload_to='images/')),
                ('rating', models.IntegerField(validators=[django.core.validators.MaxLengthValidator, django.core.validators.MinLengthValidator])),
            ],
            options={
                'abstract': False,
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='TestimonialTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('comment', models.CharField(max_length=70)),
                ('identity', models.CharField(max_length=70)),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='website.testimonial')),
            ],
            options={
                'verbose_name': 'testimonial Translation',
                'db_table': 'website_testimonial_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
    ]

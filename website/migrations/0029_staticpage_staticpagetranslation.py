# Generated by Django 4.0.2 on 2022-02-28 10:57

from django.db import migrations, models
import django.db.models.deletion
import parler.fields
import parler.models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0028_partner'),
    ]

    operations = [
        migrations.CreateModel(
            name='StaticPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('show_at_navbar', models.BooleanField(default=False)),
                ('show_at_footer', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='StaticPageTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('content', models.TextField(verbose_name='Content')),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='website.staticpage')),
            ],
            options={
                'verbose_name': 'static page Translation',
                'db_table': 'website_staticpage_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
    ]

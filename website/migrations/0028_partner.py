# Generated by Django 4.0.2 on 2022-02-28 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0027_alter_bannerhero_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('url', models.TextField(verbose_name='Url')),
                ('image', models.ImageField(upload_to='', verbose_name='Image')),
            ],
        ),
    ]

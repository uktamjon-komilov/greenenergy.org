# Generated by Django 4.0.2 on 2022-02-25 12:10

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0017_alter_processitem_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='processitem',
            name='image',
            field=django_resized.forms.ResizedImageField(crop=['middle', 'center'], force_format=None, keep_meta=True, quality=100, size=[100, 100], upload_to='images/'),
        ),
    ]

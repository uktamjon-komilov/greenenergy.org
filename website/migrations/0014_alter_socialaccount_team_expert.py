# Generated by Django 4.0.2 on 2022-02-24 22:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0013_alter_teamexpert_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialaccount',
            name='team_expert',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='links', to='website.teamexpert'),
        ),
    ]
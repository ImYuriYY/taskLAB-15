# Generated by Django 5.0 on 2023-12-22 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='gpa',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]

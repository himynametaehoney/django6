# Generated by Django 4.0.5 on 2022-06-28 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trans', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trans',
            name='text1',
            field=models.TextField(blank=True),
        ),
    ]

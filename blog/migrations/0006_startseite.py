# Generated by Django 3.2.9 on 2021-11-13 23:12

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20211113_2310'),
    ]

    operations = [
        migrations.CreateModel(
            name='Startseite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inhalt', ckeditor.fields.RichTextField(null=True)),
            ],
        ),
    ]

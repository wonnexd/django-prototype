# Generated by Django 3.2.13 on 2022-06-03 19:07

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_remove_blogpost_sidetext'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='picture',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
    ]

# Generated by Django 3.2.13 on 2022-06-13 08:02

import ckeditor.fields
import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_rename_picture_blogpost_text_with_pictures'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='maintext',
            field=ckeditor.fields.RichTextField(default=''),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='text_with_pictures',
            field=ckeditor_uploader.fields.RichTextUploadingField(default=''),
        ),
    ]

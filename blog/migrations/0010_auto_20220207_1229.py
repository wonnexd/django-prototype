# Generated by Django 3.2.12 on 2022-02-07 11:29

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_alter_blogeintrag_sidetext'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogeintrag',
            name='previewtext',
            field=ckeditor.fields.RichTextField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='blogeintrag',
            name='sidetext',
            field=ckeditor.fields.RichTextField(max_length=400, null=True),
        ),
    ]
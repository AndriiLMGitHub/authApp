# Generated by Django 3.0.7 on 2020-06-19 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postnew',
            name='image_post',
            field=models.FileField(upload_to='image_folder/'),
        ),
    ]
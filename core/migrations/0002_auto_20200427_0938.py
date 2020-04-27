# Generated by Django 3.0.5 on 2020-04-27 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image_url',
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to=''),
        ),
    ]

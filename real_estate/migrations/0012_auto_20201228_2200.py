# Generated by Django 3.0.7 on 2020-12-28 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('real_estate', '0011_auto_20201228_1252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='a_image',
            field=models.FileField(blank=True, default='noimg.jpg', null=True, upload_to='media/'),
        ),
    ]

# Generated by Django 3.0.7 on 2020-12-28 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('real_estate', '0014_auto_20201228_2208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='a_image',
            field=models.FileField(default='noimg.jpg', null=True, upload_to='images/', verbose_name=''),
        ),
    ]

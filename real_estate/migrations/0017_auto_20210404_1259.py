# Generated by Django 3.0.7 on 2021-04-04 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('real_estate', '0016_comments_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='a_image',
            field=models.FileField(default='agent-4.jpg', null=True, upload_to='images/', verbose_name=''),
        ),
    ]

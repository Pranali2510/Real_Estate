# Generated by Django 3.0.7 on 2020-12-27 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('real_estate', '0003_remove_ufeedback_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='ufeedback',
            name='description',
            field=models.TextField(default=''),
        ),
    ]
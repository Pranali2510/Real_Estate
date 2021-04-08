# Generated by Django 3.0.7 on 2020-12-27 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('real_estate', '0008_agent_a_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='a_address',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='agent',
            name='a_company_mobile',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='agent',
            name='a_mobile',
            field=models.IntegerField(default=0),
        ),
    ]
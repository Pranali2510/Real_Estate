# Generated by Django 3.0.7 on 2020-12-27 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('real_estate', '0005_auto_20201227_1217'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agent',
            name='a_address',
        ),
        migrations.RemoveField(
            model_name='agent',
            name='a_company_address',
        ),
        migrations.RemoveField(
            model_name='agent',
            name='a_company_email',
        ),
        migrations.RemoveField(
            model_name='agent',
            name='a_company_mobile',
        ),
        migrations.RemoveField(
            model_name='agent',
            name='a_company_name',
        ),
        migrations.RemoveField(
            model_name='agent',
            name='a_mobile',
        ),
        migrations.AlterField(
            model_name='property',
            name='balcony',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='balcony'),
        ),
        migrations.AlterField(
            model_name='property',
            name='lift',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='lift'),
        ),
        migrations.AlterField(
            model_name='property',
            name='masterroom',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='masterroom'),
        ),
        migrations.AlterField(
            model_name='property',
            name='parking',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='parking'),
        ),
        migrations.AlterField(
            model_name='property',
            name='storeroom',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='storeroom'),
        ),
        migrations.AlterField(
            model_name='property',
            name='swimming',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='swimming'),
        ),
    ]

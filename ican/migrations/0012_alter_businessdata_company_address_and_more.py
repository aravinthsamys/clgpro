# Generated by Django 4.2.11 on 2024-05-18 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ican', '0011_alter_businessdata_company_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businessdata',
            name='company_address',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='businessdata',
            name='company_name',
            field=models.CharField(max_length=50),
        ),
    ]

# Generated by Django 4.2 on 2024-05-26 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_account_options_alter_account_managers_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='birthday',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]

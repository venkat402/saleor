# Generated by Django 2.2.6 on 2020-04-22 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0034_service_account_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, max_length=25),
        ),
    ]

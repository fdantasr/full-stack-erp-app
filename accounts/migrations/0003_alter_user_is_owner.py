# Generated by Django 5.1.6 on 2025-02-21 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_groupe_groupe_permissions_user_groupe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_owner',
            field=models.BooleanField(default=True),
        ),
    ]

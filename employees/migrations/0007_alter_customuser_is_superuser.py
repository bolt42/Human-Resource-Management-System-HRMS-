# Generated by Django 5.0.7 on 2024-07-27 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0006_rename_first_name_customuser_firstname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]

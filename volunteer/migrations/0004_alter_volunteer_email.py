# Generated by Django 4.0.4 on 2022-05-23 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('volunteer', '0003_rename_user_volunteer_alter_volunteer_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteer',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
    ]

# Generated by Django 4.0.4 on 2022-05-23 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('volunteer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(default='some string', max_length=254),
        ),
    ]

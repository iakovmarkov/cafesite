# Generated by Django 3.1 on 2020-10-11 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0006_auto_20200919_2027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(max_length=2000),
        ),
    ]

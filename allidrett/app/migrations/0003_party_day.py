# Generated by Django 3.1 on 2020-08-28 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20200827_2102'),
    ]

    operations = [
        migrations.AddField(
            model_name='party',
            name='day',
            field=models.CharField(default='', max_length=15),
            preserve_default=False,
        ),
    ]
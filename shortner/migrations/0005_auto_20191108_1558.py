# Generated by Django 2.2.7 on 2019-11-08 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortner', '0004_auto_20191108_1333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='treyeurl',
            name='shortcode',
            field=models.CharField(blank=True, max_length=10, unique=True),
        ),
    ]

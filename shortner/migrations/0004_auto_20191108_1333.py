# Generated by Django 2.2.7 on 2019-11-08 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortner', '0003_auto_20191108_1105'),
    ]

    operations = [
        migrations.AddField(
            model_name='treyeurl',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='treyeurl',
            name='shortcode',
            field=models.CharField(blank=True, max_length=15, unique=True),
        ),
    ]

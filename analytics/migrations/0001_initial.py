# Generated by Django 2.2.7 on 2019-11-09 00:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shortner', '0006_auto_20191109_0515'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClickEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=0)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('treye_url', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='shortner.TreyeURL')),
            ],
        ),
    ]

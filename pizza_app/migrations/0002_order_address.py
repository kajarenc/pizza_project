# Generated by Django 2.1.3 on 2018-11-10 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.CharField(default='Moscow, Russia', max_length=256),
        ),
    ]

# Generated by Django 2.2.1 on 2019-07-17 09:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190717_0120'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='important',
        ),
    ]

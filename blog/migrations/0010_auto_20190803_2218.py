# Generated by Django 2.2.1 on 2019-08-04 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20190802_0407'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='postcategory',
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('Personal', 'Personal'), ('Hairstyle', 'Hairstyle'), ('Makeup', 'Makeup')], default='Hairstyle', max_length=15),
        ),
        migrations.DeleteModel(
            name='PostCategory',
        ),
    ]
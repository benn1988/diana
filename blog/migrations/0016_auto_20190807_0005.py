# Generated by Django 2.2.1 on 2019-08-07 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20190806_2354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('personal', 'Personal'), ('hairstyle', 'Hairstyle'), ('makeup', 'Makeup')], default='hairstyle', max_length=10),
        ),
    ]
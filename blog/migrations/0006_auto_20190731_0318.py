# Generated by Django 2.2.1 on 2019-07-31 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20190731_0302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_photo',
            field=models.ImageField(default='default_blog.jpg', upload_to='post_photo'),
        ),
    ]

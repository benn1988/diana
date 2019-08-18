# Generated by Django 2.2.4 on 2019-08-13 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_content', '0002_auto_20190813_0121'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='photocateg',
            options={'verbose_name': 'Photo Category', 'verbose_name_plural': 'Photo Categories'},
        ),
        migrations.RenameField(
            model_name='photo',
            old_name='date_posted',
            new_name='date_uploaded',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='post_photo',
        ),
        migrations.AddField(
            model_name='photo',
            name='jpg_photo',
            field=models.ImageField(default='default-blog.jpg', upload_to='gallery_jpg'),
        ),
        migrations.AddField(
            model_name='photo',
            name='webp_photo',
            field=models.ImageField(default='default-blog.jpg', upload_to='gallery_webp'),
        ),
    ]

# Generated by Django 5.0.2 on 2024-03-22 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatter', '0025_image_remove_post_image_delete_images_post_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
        migrations.DeleteModel(
            name='Image',
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/posts'),
        ),
    ]

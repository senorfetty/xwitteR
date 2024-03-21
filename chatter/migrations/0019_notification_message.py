# Generated by Django 5.0.2 on 2024-03-21 10:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatter', '0018_remove_notification_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='message',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='chatter.message'),
        ),
    ]

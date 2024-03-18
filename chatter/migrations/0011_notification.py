# Generated by Django 5.0.2 on 2024-03-18 14:23

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatter', '0010_comment_parent'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notification_type', models.IntegerField(choices=[(0, 'Comment'), (1, 'Like'), (2, 'Follow')])),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('user_has_seen', models.BooleanField(default=False)),
                ('from_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notification_from', to='chatter.account')),
                ('post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='chatter.comment')),
                ('to_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notification_to', to='chatter.account')),
            ],
        ),
    ]

# Generated by Django 4.2.5 on 2023-10-01 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0011_event_duration'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='date_time',
            new_name='end_date_time',
        ),
        migrations.RemoveField(
            model_name='event',
            name='duration',
        ),
        migrations.AddField(
            model_name='event',
            name='start_date_time',
            field=models.DateTimeField(default="1970-01-01 00:00:00"),
            preserve_default=False,
        ),
    ]

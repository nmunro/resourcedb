# Generated by Django 4.2.3 on 2023-07-30 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0003_remove_event_slug_remove_location_slug_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='organisation',
            name='logo',
            field=models.ImageField(default='', upload_to='logos'),
            preserve_default=False,
        ),
    ]
# Generated by Django 4.2.3 on 2023-07-31 16:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('info', '0007_rename_friends_organisation_users'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organisation',
            name='users',
        ),
        migrations.AddField(
            model_name='organisation',
            name='admin',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]

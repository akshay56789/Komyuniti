# Generated by Django 5.0.4 on 2024-05-17 17:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0040_user_request_report_reason_alter_groups_theme'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_request',
            name='club_post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.club_post'),
        ),
    ]

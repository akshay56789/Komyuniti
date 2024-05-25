# Generated by Django 5.0.4 on 2024-04-29 19:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0028_remove_post_comments_alter_comments_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_request',
            name='club',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.club'),
        ),
        migrations.AlterField(
            model_name='user_request',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.groups'),
        ),
    ]

# Generated by Django 5.0.4 on 2024-05-16 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0033_club_post_post_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club_post',
            name='post_updated',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]

# Generated by Django 4.1.1 on 2024-03-29 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_user_bio_user_name_alter_user_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='', null=True, upload_to=''),
        ),
    ]

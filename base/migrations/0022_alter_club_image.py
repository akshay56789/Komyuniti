# Generated by Django 5.0.4 on 2024-04-24 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0021_alter_club_private'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='image',
            field=models.FileField(default='komyuniti-post-image/avatar_mclyfi.jpg', upload_to='komyuniti-club-image'),
        ),
    ]

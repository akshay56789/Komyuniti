# Generated by Django 4.1.1 on 2024-04-05 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_alter_club_desciption'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='club',
            name='desciption',
        ),
        migrations.AddField(
            model_name='club',
            name='description',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]

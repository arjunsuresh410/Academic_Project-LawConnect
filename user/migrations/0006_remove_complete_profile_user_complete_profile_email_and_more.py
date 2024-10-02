# Generated by Django 5.0.2 on 2024-03-13 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_delete_reply'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='complete_profile',
            name='user',
        ),
        migrations.AddField(
            model_name='complete_profile',
            name='email',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='complete_profile',
            name='first_name',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='complete_profile',
            name='image',
            field=models.ImageField(default='', upload_to='profile/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='complete_profile',
            name='password',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]

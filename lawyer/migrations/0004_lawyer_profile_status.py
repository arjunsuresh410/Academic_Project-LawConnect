# Generated by Django 3.2.4 on 2024-04-11 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lawyer', '0003_reply'),
    ]

    operations = [
        migrations.AddField(
            model_name='lawyer_profile',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]

# Generated by Django 2.0.3 on 2018-04-08 12:15

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='following',
            name='followed',
            field=models.ManyToManyField(related_name='followed_user', to=settings.AUTH_USER_MODEL),
        ),
    ]

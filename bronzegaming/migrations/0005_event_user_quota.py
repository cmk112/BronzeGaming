# Generated by Django 2.1.7 on 2019-03-02 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bronzegaming', '0004_auto_20190301_2020'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='user_quota',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
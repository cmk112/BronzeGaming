# Generated by Django 2.1.7 on 2019-03-02 05:08

from django.db import migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('bronzegaming', '0007_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='image',
            field=sorl.thumbnail.fields.ImageField(upload_to='./games/'),
        ),
        migrations.AlterField(
            model_name='platform',
            name='image',
            field=sorl.thumbnail.fields.ImageField(upload_to='./games/'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=sorl.thumbnail.fields.ImageField(null=True, upload_to='./profiles/'),
        ),
    ]
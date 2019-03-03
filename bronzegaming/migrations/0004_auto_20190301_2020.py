# Generated by Django 2.1.7 on 2019-03-02 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bronzegaming', '0003_auto_20190301_1816'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='body',
            field=models.TextField(default='tester'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='game',
            name='image',
            field=models.ImageField(upload_to='./games/'),
        ),
        migrations.AlterField(
            model_name='platform',
            name='image',
            field=models.ImageField(upload_to='./games/'),
        ),
    ]

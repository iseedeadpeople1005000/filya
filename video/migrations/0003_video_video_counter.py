# Generated by Django 2.1.4 on 2019-02-12 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0002_auto_20190212_1701'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='Video_counter',
            field=models.IntegerField(default=0),
        ),
    ]

# Generated by Django 2.1.4 on 2019-02-13 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0003_video_video_counter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='Comment_text',
            field=models.TextField(max_length=1000, verbose_name=''),
        ),
    ]

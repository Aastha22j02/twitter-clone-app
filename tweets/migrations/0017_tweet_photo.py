# Generated by Django 3.2.4 on 2023-07-15 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0016_remove_tweet_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='tweet_photos'),
        ),
    ]

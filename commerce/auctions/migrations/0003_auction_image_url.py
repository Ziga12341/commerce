# Generated by Django 4.1 on 2023-03-02 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_auction_auctioncategories_comment_bid_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction',
            name='image_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]

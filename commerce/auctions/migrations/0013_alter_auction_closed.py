# Generated by Django 4.1 on 2023-03-04 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0012_comment_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='closed',
            field=models.BooleanField(default=False),
        ),
    ]

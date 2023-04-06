# Generated by Django 4.1.7 on 2023-04-06 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0012_author_username_alter_news_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='username',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]

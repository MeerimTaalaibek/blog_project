# Generated by Django 3.2.3 on 2021-05-31 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_api', '0005_post_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='preview',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]

# Generated by Django 4.1.5 on 2023-01-19 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blog_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='icon',
            field=models.ImageField(upload_to='media/blog/'),
        ),
    ]
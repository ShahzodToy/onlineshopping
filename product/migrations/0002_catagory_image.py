# Generated by Django 5.0.6 on 2024-06-05 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='catagory',
            name='image',
            field=models.ImageField(default=1, upload_to='category'),
            preserve_default=False,
        ),
    ]

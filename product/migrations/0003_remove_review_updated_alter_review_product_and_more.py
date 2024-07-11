# Generated by Django 4.2.13 on 2024-06-12 15:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_catagory_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='updated',
        ),
        migrations.AlterField(
            model_name='review',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review_product', to='product.product'),
        ),
        migrations.DeleteModel(
            name='ProductSizes',
        ),
    ]

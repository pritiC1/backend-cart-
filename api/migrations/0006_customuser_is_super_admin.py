# Generated by Django 5.1.2 on 2024-10-28 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_product_brand_product_category_product_color_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_super_admin',
            field=models.BooleanField(default=False),
        ),
    ]

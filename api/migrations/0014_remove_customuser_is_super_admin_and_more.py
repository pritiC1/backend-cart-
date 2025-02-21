# Generated by Django 5.1.2 on 2024-11-14 06:27

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_product_liked_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='is_super_admin',
        ),
        migrations.AlterField(
            model_name='product',
            name='liked_by',
            field=models.ManyToManyField(blank=True, related_name='liked_products', to=settings.AUTH_USER_MODEL),
        ),
    ]

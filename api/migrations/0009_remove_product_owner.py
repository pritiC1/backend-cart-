# Generated by Django 5.1.2 on 2024-11-10 09:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_alter_product_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='owner',
        ),
    ]

# Generated by Django 4.1.5 on 2023-02-05 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_remove_product_digital_product_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='digital',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
    ]

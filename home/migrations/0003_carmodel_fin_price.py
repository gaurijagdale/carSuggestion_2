# Generated by Django 5.0.3 on 2024-04-23 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_remove_brand_description_remove_brand_logo_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='carmodel',
            name='fin_price',
            field=models.FloatField(null=True),
        ),
    ]

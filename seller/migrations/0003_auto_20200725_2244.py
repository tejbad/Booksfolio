# Generated by Django 3.0.2 on 2020-07-25 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0002_auto_20200718_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller_books',
            name='publish_yr',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]

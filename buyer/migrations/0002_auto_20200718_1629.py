# Generated by Django 3.0.8 on 2020-07-18 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buyer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyer_data',
            name='sem',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='buyer_data',
            name='sub',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='buyer_data',
            name='year',
            field=models.CharField(max_length=10),
        ),
        migrations.DeleteModel(
            name='Subject',
        ),
        migrations.DeleteModel(
            name='Year',
        ),
    ]

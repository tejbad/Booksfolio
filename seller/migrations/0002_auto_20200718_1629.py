# Generated by Django 3.0.8 on 2020-07-18 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='seller_books',
            old_name='stream',
            new_name='product_type',
        ),
        migrations.RenameField(
            model_name='seller_books',
            old_name='book_yr',
            new_name='shown_price',
        ),
        migrations.AddField(
            model_name='seller_books',
            name='disc',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='seller_books',
            name='domain',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='seller_books',
            name='is_ordered',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='seller_books',
            name='manufacturer',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='seller_books',
            name='manufacturer_yr',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='seller_books',
            name='publish_yr',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='seller_books',
            name='yr_sem',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='seller_books',
            name='author_name',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='seller_books',
            name='book_img',
            field=models.ImageField(blank=True, default='', upload_to='Book_img'),
        ),
        migrations.AlterField(
            model_name='seller_books',
            name='branch',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]

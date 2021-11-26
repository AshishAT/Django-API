# Generated by Django 3.2.9 on 2021-11-25 21:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_book_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('registration_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('product_id', models.CharField(max_length=100)),
                ('quntity', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Product_Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.CharField(max_length=100)),
                ('product_name', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=100)),
                ('brand_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.brand')),
                ('category_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.product_category')),
            ],
        ),
        migrations.DeleteModel(
            name='userdetails',
        ),
    ]
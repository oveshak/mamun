# Generated by Django 5.1.1 on 2024-10-11 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Checkout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('address', models.CharField(max_length=255)),
                ('address2', models.CharField(blank=True, max_length=255)),
                ('country', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('zip_code', models.CharField(max_length=20)),
                ('payment_method', models.CharField(max_length=20)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]

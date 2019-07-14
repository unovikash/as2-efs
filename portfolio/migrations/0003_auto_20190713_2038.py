# Generated by Django 2.0.5 on 2019-07-14 01:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_investment_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investment',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='investment_customer', to='portfolio.Customer'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stock_customer', to='portfolio.Customer'),
        ),
    ]
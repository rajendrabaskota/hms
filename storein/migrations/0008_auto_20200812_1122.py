# Generated by Django 3.0.8 on 2020-08-12 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storein', '0007_medicine_present_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoicein',
            name='entry_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='invoicein',
            name='invoice_date',
            field=models.DateField(null=True),
        ),
    ]

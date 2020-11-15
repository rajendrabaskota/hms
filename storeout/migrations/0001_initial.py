# Generated by Django 3.0.8 on 2020-08-04 05:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('storein', '0007_medicine_present_quantity'),
    ]

    operations = [
        migrations.CreateModel(
            name='InvoiceOut',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=150)),
                ('total_amount', models.FloatField()),
                ('user', models.CharField(max_length=150, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='InvoiceOutDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_out', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='storeout.InvoiceOut')),
                ('medicine', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='storein.Medicine')),
            ],
        ),
    ]

# Generated by Django 3.1.4 on 2021-04-19 09:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Lakshma_ERP_App', '0006_auto_20210419_0217'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ompocostdetail',
            old_name='product_id',
            new_name='product_name_short',
        ),
        migrations.RemoveField(
            model_name='ompocostdetail',
            name='cm_per_unit_per',
        ),
        migrations.RemoveField(
            model_name='ompocostdetail',
            name='price_per_unit_per',
        ),
        migrations.AlterField(
            model_name='wopocountrydetails',
            name='country_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lib_country_code', to='Lakshma_ERP_App.libcountry'),
        ),
        migrations.AlterField(
            model_name='wopocountrydetails',
            name='product_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inv_product_code', to='Lakshma_ERP_App.invproductinfo'),
        ),
    ]
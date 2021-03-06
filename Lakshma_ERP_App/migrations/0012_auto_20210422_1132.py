# Generated by Django 3.1.4 on 2021-04-22 05:32

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Lakshma_ERP_App', '0011_auto_20210421_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hrmemployee',
            name='confirmation_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='hrmemployee',
            name='date_of_birth',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='hrmemployee',
            name='joining_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='ompocostdetail',
            name='product_name_short',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inv_product_name', to='Lakshma_ERP_App.invproductinfo'),
        ),
        migrations.AlterField(
            model_name='ompolabdipinfo',
            name='color_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='libdip_color_name', to='Lakshma_ERP_App.libcolor'),
        ),
    ]

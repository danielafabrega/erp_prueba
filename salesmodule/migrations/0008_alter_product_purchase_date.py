# Generated by Django 3.2.7 on 2021-10-04 07:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('salesmodule', '0007_auto_20211004_0723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='purchase_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
# Generated by Django 3.2.7 on 2021-10-04 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salesmodule', '0004_alter_kardex_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='kardex',
            old_name='document',
            new_name='t_document',
        ),
        migrations.AddField(
            model_name='kardex',
            name='number',
            field=models.IntegerField(default=0),
        ),
    ]

# Generated by Django 3.0.7 on 2020-06-04 16:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0011_auto_20200604_1634'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sale',
            options={},
        ),
        migrations.RemoveField(
            model_name='sale',
            name='product',
        ),
        migrations.RemoveField(
            model_name='sale',
            name='quantity',
        ),
    ]

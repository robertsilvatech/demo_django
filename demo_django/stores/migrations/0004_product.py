# Generated by Django 3.0.7 on 2020-06-04 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0003_consolidadesale_store'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]

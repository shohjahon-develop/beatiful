# Generated by Django 4.2.6 on 2023-10-21 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Maxsulotlar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('bio', models.CharField(max_length=300)),
                ('img', models.ImageField(upload_to='products/img')),
                ('cost', models.IntegerField()),
            ],
        ),
    ]

# Generated by Django 4.2.6 on 2023-10-21 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('bio', models.CharField(max_length=500)),
                ('img', models.ImageField(upload_to='client/img')),
            ],
        ),
    ]

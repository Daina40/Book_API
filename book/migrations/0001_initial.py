# Generated by Django 4.2.7 on 2023-11-23 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('price', models.PositiveIntegerField()),
                ('writer_name', models.CharField(max_length=50)),
                ('stock', models.PositiveIntegerField()),
            ],
        ),
    ]

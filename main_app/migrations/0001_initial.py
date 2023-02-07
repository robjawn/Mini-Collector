# Generated by Django 4.1.5 on 2023-02-01 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mini',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('kind', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=500)),
                ('price', models.CharField(max_length=600)),
                ('image', models.CharField(max_length=600)),
            ],
        ),
    ]
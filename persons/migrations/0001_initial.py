# Generated by Django 3.2.6 on 2021-08-22 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identification_card', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=150)),
                ('surnames', models.CharField(max_length=150)),
                ('birth_date', models.DateField()),
                ('address', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('institution', models.CharField(max_length=255)),
                ('accumulated_miles', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
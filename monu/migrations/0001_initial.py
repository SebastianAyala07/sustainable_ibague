# Generated by Django 3.2.6 on 2021-08-23 03:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('persons', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('license_plate', models.CharField(max_length=6, unique=True)),
                ('model', models.IntegerField()),
                ('brand', models.CharField(max_length=200)),
                ('type_vehicle', models.CharField(max_length=110)),
                ('photo', models.ImageField(upload_to='vehicles/')),
                ('maximum_passengers', models.IntegerField()),
                ('fuel_type', models.CharField(max_length=255)),
                ('available', models.BooleanField(default=True)),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='persons.driver')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('address', models.CharField(max_length=255)),
                ('students_id', models.ManyToManyField(blank=True, to='persons.Student')),
                ('vehicle_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='monu.vehicle')),
            ],
        ),
    ]
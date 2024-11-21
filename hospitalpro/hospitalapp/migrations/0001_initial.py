# Generated by Django 5.1.1 on 2024-10-29 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PatientsData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patients_name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=50)),
                ('mobile', models.BigIntegerField()),
                ('blood_group', models.CharField(max_length=50)),
                ('doctors_name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('problem', models.CharField(max_length=50)),
            ],
        ),
    ]
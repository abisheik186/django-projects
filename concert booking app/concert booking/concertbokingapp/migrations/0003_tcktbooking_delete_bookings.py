# Generated by Django 4.2.4 on 2023-09-13 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('concertbokingapp', '0002_bookings'),
    ]

    operations = [
        migrations.CreateModel(
            name='tcktbooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('concerttitle', models.CharField(max_length=50)),
                ('count', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='bookings',
        ),
    ]

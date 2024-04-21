# Generated by Django 2.1.15 on 2024-04-16 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('appointment_day', models.CharField(choices=[('Monday', 'Monday'), ('Wednesday', 'Wednesday'), ('Friday', 'Friday')], max_length=20)),
            ],
        ),
    ]

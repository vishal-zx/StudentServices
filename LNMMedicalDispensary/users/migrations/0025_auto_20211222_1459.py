# Generated by Django 3.2.7 on 2021-12-22 09:29

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0024_merge_0022_user_uid_0023_auto_20211222_1436'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='uid',
        ),
        migrations.CreateModel(
            name='MedicalCertificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.TextField()),
                ('fromdate', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('todate', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('Did', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.doctor')),
                ('Pid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.patient')),
            ],
        ),
    ]

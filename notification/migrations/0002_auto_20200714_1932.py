# Generated by Django 3.0.8 on 2020-07-14 14:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0001_initial'),
        ('notification', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='staff',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staff.Staff', verbose_name='Assigned To'),
        ),
    ]
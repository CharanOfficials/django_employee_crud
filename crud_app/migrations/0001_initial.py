# Generated by Django 4.2 on 2024-01-11 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tbl_Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('email', models.CharField(max_length=250)),
                ('mobile_no', models.IntegerField(max_length=12)),
            ],
            options={
                'db_table': 'tbl_employee',
            },
        ),
    ]

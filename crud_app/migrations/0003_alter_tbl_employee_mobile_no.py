# Generated by Django 4.2 on 2024-01-11 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud_app', '0002_alter_tbl_employee_mobile_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_employee',
            name='mobile_no',
            field=models.CharField(),
        ),
    ]

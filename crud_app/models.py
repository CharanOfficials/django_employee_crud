from django.db import models

# Create your models here.


class Tbl_Employee(models.Model):
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=250, null=False)
    mobile_no = models.CharField(null=False)

    class Meta:
        db_table = 'tbl_employee'

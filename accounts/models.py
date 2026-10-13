from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):

    class Role(models.TextChoices):
        CUSTOMER="customer","Customer"
        SELLER="seller","Seller"
        ADMIN="admin","Admin"

    role=models.CharField(max_length=20,choices=Role.choices,default=Role.CUSTOMER,db_index=True)

    def __str__(self):
        return self.username

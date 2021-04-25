from django.db import models
from datetime import datetime
# Create your models here.
class Student(models.Model):
    registration_number = models.CharField(max_length=11,
                                            primary_key = True,
                                            verbose_name = "Registration Number"
                                            )
    name = models.CharField(max_length=200, verbose_name = "Name")
    email = models.EmailField(max_length=200, verbose_name = "Email")
    home_town = models.CharField(max_length=200, verbose_name = "Home town")
    score = models.IntegerField(default=0, verbose_name = "Score")
    date_of_birth =  models.DateField(verbose_name = "Date of Birth")
    register_date = models.DateTimeField(default=datetime.now())
    modify_date = models.DateTimeField(null=True)
    is_delete = models.BooleanField(default=False)
    def __str__(self):
        return self.name

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class management(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=50)
    roll_number=models.IntegerField(unique=True)
    department=models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    admission_date=models.DateField()
    details=models.TextField(default='Click Here...')
    
    def __str__(self):
       return self.name
from django.db import models

# Create your models here.

class Login(models.Model):
       userName=models.CharField(max_length=30)
       email=models .CharField(max_length=30)
       password=models.CharField(max_length=30)
       
       def __str__(self):
            return self.userName
       
       
class Class(models.Model):
        session=models.CharField(max_length=30)
        
        def __str__(self):
            return self.session
            
class Student(models.Model):
        name =models.CharField(max_length=30, unique=False)
        session=models.ForeignKey("Class",on_delete=models.PROTECT)
        
        def __str__(self):
            return self.name,self.session
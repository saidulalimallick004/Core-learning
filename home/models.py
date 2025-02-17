from django.db import models

# Create your models here.

class students(models.Model):
    
    Name=models.CharField(max_length=100)
    Age=models.IntegerField(null=True)
    Email=models.EmailField()
    Add=models.TextField(null=True,blank=True)
    
    
    

class course(models.Model):
    CourseId=models.CharField(max_length=5)
    CourseName=models.CharField(max_length=50)
    FileNotes=models.FileField(null=True)
    
    
class cars(models.Model):
    Name=models.CharField(max_length=10)
    Color=models.TextField()
    
    
    
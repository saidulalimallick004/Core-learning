from django.db import models

# Create your models here.




class recipe(models.Model):
    Name=models.CharField(max_length=50)
    Descriptions=models.TextField()

    R_Image=models.ImageField (upload_to="thumbnail")
    
    
    def __str__(self)-> str:
        return self.Name
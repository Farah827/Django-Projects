from django.db import models

# Create your models here.
class Book(models.Model):
    title= models.CharField(max_length=250)
    desc= models.CharField(max_length=255)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"Book Title: {self.title}"
    

class Author(models.Model):
    first_name= models.CharField(max_length=45)
    last_name= models.CharField(max_length=45)
    books= models.ManyToManyField(Book , related_name='authors')
    notes= models.CharField(max_length=255 , null=True)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"Author Name:{self.first_name} {self.last_name}"
    
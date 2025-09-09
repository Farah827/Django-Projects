from django.db import models

# Create your models here.
class Show(models.Model):
    title = models.CharField(max_length=50)
    network =models.CharField(max_length=50)
    release_date=models.DateField()
    desc=models.CharField(max_length=255 , null=True )
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return super().__str__()

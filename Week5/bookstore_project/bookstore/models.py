from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', related_name='books', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2)     
    published_date = models.DateField()
    isbn = models.CharField(max_length=20)
    
    
    def __str__(self):
        return self.title
    
class  Author(models.Model) :
    name =models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
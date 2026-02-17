from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone

class Author(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
 
class Book(models.Model):
    title = models.CharField(max_length=200)
    isbn =models.CharField(max_length=50)  
    author =models.ForeignKey(Author, on_delete=models.CASCADE)
    categories =models.ManyToManyField(Category)
    available_copies =models.IntegerField(default=1) 
    
    def __str__(self):
        return self.title
    
class Member(models.Model):
    name =models.CharField(max_length=200) 
    email =models.EmailField()
    
    def __str__(self):
        return self.name
        
class Loan(models.Model):
    book =models.ForeignKey(Book,on_delete=models.CASCADE)
    member =models.ForeignKey(Member,on_delete=models.CASCADE)
    
    loan_date = models.DateField(default=timezone.now)
    return_date =models.DateField(null=True,blank=True)
    
    def __str__(self):
        return f"{self.book.title} → {self.member.name}"
        
        
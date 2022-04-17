from django.db import models

# Create your models here.
class Books(models.Model):
    id= models.CharField(max_length=20,primary_key=True)
    book_name=models.CharField(max_length=100)
    edition=models.CharField(max_length=10)
    author_name=models.CharField(max_length=20)

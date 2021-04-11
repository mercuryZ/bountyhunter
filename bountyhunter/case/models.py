from django.db import models
# from django.core.validations import 

# Create your models here.
class Case(models.Model):
    case_name = models.CharField(max_length=50, unique=True)
    hunter = models.EmailField(max_length=254) 
    date_from = models.DateTimeField()
    date_to   = models.DateTimeField() 
    active    = models.BooleanField()

    def __str__(self):
        return self.case_name
    
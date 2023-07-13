from django.db import models

# Create your models here.
class Item(models.Model):
    name=models.CharField(max_length=200)
    price=models.IntegerField()
    Order=models.BooleanField()
    contact_no=models.IntegerField()
    def _str_(self):
        return self.name
    
# class contact(models.Model):
#     name=models.CharField(max_length=200)
#     email=models.CharField(max_length=200)
#     subject=models.CharField(max_length=200)
#     message=models.CharField(max_length=200)
#     def _str_(self):
#         return self.name
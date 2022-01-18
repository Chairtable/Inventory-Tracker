from django.db import models

class Inventory(models.Model):  
    iid = models.CharField(max_length=20)  
    iname = models.CharField(max_length=100)  
    iquantity = models.IntegerField()
    class Meta:  
        db_table = "inventory"  

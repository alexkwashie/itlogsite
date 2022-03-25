from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class All_equipment(models.Model):
    assigned_to = models.CharField(max_length=100)
    asset_no = models.CharField(max_length=100)
    device_type = models.CharField(max_length=100)
    device_make = models.CharField(max_length=100)
    device_model = models.CharField(max_length=100)
    location_status = models.CharField(max_length=100)
    serial_no = models.CharField(max_length=100)    
    purchase_reason = models.TextField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True, blank=True)  
    price = models.DecimalField(max_digits= 10, decimal_places=2,blank=True)
    in_service= models.BooleanField(default=False)
    image = models.ImageField(upload_to ='eq_images/',blank=True)
    date_assigned = models.DateField(blank=True, null=True,auto_now_add=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.asset_no
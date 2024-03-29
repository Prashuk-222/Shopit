from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinLengthValidator
# Create your models here.
state_choices = (("Andhra Pradesh","Andhra Pradesh"),
                 ("Arunachal Pradesh ","Arunachal Pradesh "),
                 ("Assam","Assam"),
                 ("Bihar","Bihar"),
                 ("Chhattisgarh","Chhattisgarh"),
                 ("Goa","Goa"),
                 ("Gujarat","Gujarat"),
                 ("Haryana","Haryana"),
                 ("Himachal Pradesh","Himachal Pradesh"),
                 ("Jammu and Kashmir ","Jammu and Kashmir "),
                 ("Jharkhand","Jharkhand"),
                 ("Karnataka","Karnataka"),
                 ("Kerala","Kerala"),
                 ("Madhya Pradesh","Madhya Pradesh"),
                 ("Maharashtra","Maharashtra"),
                 ("Manipur","Manipur"),
                 ("Meghalaya","Meghalaya"),
                 ("Mizoram","Mizoram"),
                 ("Nagaland","Nagaland"),
                 ("Odisha","Odisha"),
                 ("Punjab","Punjab"),
                 ("Rajasthan","Rajasthan"),
                 ("Sikkim","Sikkim"),
                 ("Tamil Nadu","Tamil Nadu"),
                 ("Telangana","Telangana"),
                 ("Tripura","Tripura"),
                 ("Uttar Pradesh","Uttar Pradesh"),
                 ("Uttarakhand","Uttarakhand"),
                 ("West Bengal","West Bengal"),
                 ("Andaman and Nicobar Islands","Andaman and Nicobar Islands"),
                 ("Chandigarh","Chandigarh"),
                 ("Dadra and Nagar Haveli","Dadra and Nagar Haveli"),
                 ("Daman and Diu","Daman and Diu"),
                 ("Lakshadweep","Lakshadweep"),
                 ("National Capital Territory of Delhi","National Capital Territory of Delhi"),
                 ("Puducherry","Puducherry"))

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=50)
    state = models.CharField( choices= state_choices,max_length=50)
    
def __str__(self):
    return str(self.id)

Category_choices = (
    ('M','Mobile'),
    ('L','Laptop'),
    ('TW','Top Wear'),
    ('BW','Bottom Wear'),
)

class Product(models.Model):
    title = models.CharField( max_length=100) 
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    brand = models.CharField( max_length=100)
    category = models.CharField(max_length=2,choices = Category_choices)
    product_image = models.ImageField( upload_to='producting', height_field=None, width_field=None, max_length=None)

def __strt__(self):
    return str(self.id)

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  
    quantity = models.PositiveIntegerField(default=1)

def __str__(self):
    return str(self.id)


status_choices = (
    ('Accepted','Accepted'),
    ('Packed','Packed'),
    ('On the Way','On the Way'),
    ('Deliverd','Deliverd'),
    ('Cancel','Cancel'),
)

class OrderPlaced(models.Model):
    user = models.ForeignKey( User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    ordered_date = models.DateTimeField( auto_now=False, auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    status = models.CharField(choices=status_choices, max_length=50,default='Pending') 

def __str__(self):
    return str(self.id)
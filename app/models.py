from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator

STATE_CHOICES = (
   ("AN","Andaman and Nicobar Islands"),
   ("AP","Andhra Pradesh"),
   ("AR","Arunachal Pradesh"),
   ("AS","Assam"),
   ("BR","Bihar"),
   ("CG","Chhattisgarh"),
   ("CH","Chandigarh"),
   ("DN","Dadra and Nagar Haveli"),
   ("DD","Daman and Diu"),
   ("DL","Delhi"),
   ("GA","Goa"),
   ("GJ","Gujarat"),
   ("HR","Haryana"),
   ("HP","Himachal Pradesh"),
   ("JK","Jammu and Kashmir"),
   ("JH","Jharkhand"),
   ("KA","Karnataka"),
   ("KL","Kerala"),
   ("LA","Ladakh"),
   ("LD","Lakshadweep"),
   ("MP","Madhya Pradesh"),
   ("MH","Maharashtra"),
   ("MN","Manipur"),
   ("ML","Meghalaya"),
   ("MZ","Mizoram"),
   ("NL","Nagaland"),
   ("OD","Odisha"),
   ("PB","Punjab"),
   ("PY","Pondicherry"),
   ("RJ","Rajasthan"),
   ("SK","Sikkim"),
   ("TN","Tamil Nadu"),
   ("TS","Telangana"),
   ("TR","Tripura"),
   ("UP","Uttar Pradesh"),
   ("UK","Uttarakhand"),
   ("WB","West Bengal")
)

class CustomerInfo(models.Model):
    user = models.ForeignKey(User,on_delete= models.CASCADE)
    name = models.CharField(max_length=100)
    locality = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES,max_length=5)

    def __str__(self):
        return str(self.id)
    

CATEGORY_CHOICES=(('MOB','Mobiles'),('LAP','Laptops'),('WCH','Watches'),('EB','Earbuds'))

class Product(models.Model):
    category = models.CharField(choices=CATEGORY_CHOICES,max_length=5)
    product_name = models.CharField(max_length=100)
    description = models.TextField()
    brand = models.CharField(max_length=100)
    MRP = models.FloatField()
    discounted_price = models.FloatField()
    images = models.ImageField(upload_to='uploaded product images')

    def __str__(self):
        return str(self.id)
    

class Cart(models.Model):
    user = models.ForeignKey(User,on_delete= models.CASCADE)
    product = models.ForeignKey(Product,on_delete= models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)
    
    def total_cost(self):
        return self.quantity*self.product.discounted_price


STATUS_CHOICE = (('Accepted','Accepted'),('Packed','Packed'),('On The Way','On The Way'),('Delivered','Delivered'),('Cancel','Cancel'))

class OrderPlaced(models.Model):
    user = models.ForeignKey(User,on_delete= models.CASCADE)
    product = models.ForeignKey(Product,on_delete= models.CASCADE)
    customer_info = models.ForeignKey(CustomerInfo,on_delete= models.CASCADE)
    status = models.CharField(max_length=15,choices=STATUS_CHOICE, default='pending')
    quantity=models.IntegerField(null=True)
    ordered_date = models.DateTimeField(auto_now_add=True)
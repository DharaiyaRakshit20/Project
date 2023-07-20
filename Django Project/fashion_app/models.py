from django.db import models
from seller_app.models import *
# Create your models here.


#==================Buyer Register Model Table=====================
class Register(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=100)
    conformpassword=models.CharField(max_length=100)
    propic=models.FileField(upload_to="media/", default="defult.jpg")

    def __str__(self):
        return self.email
    
#==================Cehck Out Details Model Table=====================
class Details(models.Model):
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    country=models.CharField(max_length=25)
    address=models.CharField(max_length=200)
    second_address=models.CharField(max_length=200,null=True)
    city=models.CharField(max_length=20)
    state=models.CharField(max_length=25)
    postcode=models.IntegerField(default=0)
    phone=models.CharField(max_length=124)
    email=models.CharField(max_length=50)
    order_id=models.CharField(max_length=20)
    buyer_id=models.ForeignKey(Register,on_delete=models.CASCADE)

    def __str__(self):
        return self.firstname
    


#==================Buyer Cart Model Table=====================
class Cart(models.Model):
    product_id=models.ForeignKey(Listing_Catlog,on_delete=models.CASCADE,null=True)
    Details_id=models.ForeignKey(Details,on_delete=models.CASCADE,null=True)
    buyer_id=models.ForeignKey(Register,on_delete=models.CASCADE)
    qty=models.IntegerField(default=0)
    product_color=models.CharField(max_length=50,null=True)
    product_size=models.CharField(max_length=50,null=True)
    stetus=models.BooleanField(default=True)
    total=models.IntegerField(default=0)
    
    def __str__(self):
        return str(self.buyer_id)
    
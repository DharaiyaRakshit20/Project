from django.db import models
from fashion_app.models import *


#==================Seller Register Model Table=====================
class Seller_Register(models.Model):
    seller_name=models.CharField(max_length=50)
    seller_email=models.EmailField(unique=True)
    seller_password=models.CharField(max_length=100)
    seller_conformpassword=models.CharField(max_length=100)
    seller_propic=models.FileField(upload_to="seller/", default="seller/defult.jpg")

    def __str__(self):
        return self.seller_email


#==================Catlog Listing Model Table=====================
class Listing_Catlog(models.Model):
    Catlog_Image=models.FileField(upload_to="Listing/", default="Listing/defult.jpg")
    Catlog_Name=models.CharField(max_length=50)
    Catlog_Price=models.IntegerField(default=0)
    Catlog_Sale_Price=models.CharField(max_length=50)
    Catlog_Quntity=models.CharField(max_length=50)
    Catlog_Catgary=models.CharField(max_length=50,null=True)
    Catlog_Branding=models.CharField(max_length=50,null=True)
    Catlog_Tags=models.CharField(max_length=50,null=True)


    #==========Sizes=========
    Size=[("XS","XS"),("S","S"),("M","M"),("L","L"),("XL","XL"),("XXL","XXL"),("XXXL","XXXL")]
    Catlog_Size=models.CharField(max_length=100,choices=Size,blank=True,)

    #==========Color==========
    Color=[("Black","Black"),("White","White"),("Yellow","Yellow"),("Blue","Blue"),("Red","Red"),("Green","Green")]
    Catlog_Color=models.CharField(max_length=100,choices=Color,blank=True)

    Catlog_Fabric=models.CharField(max_length=50)
    Catlog_Discription=models.CharField(max_length=500,null=True)
    seller=models.ForeignKey(Seller_Register, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.Catlog_Name
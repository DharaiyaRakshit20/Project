from django.shortcuts import render
from .models import *
from django.conf import settings
from django.core.mail import send_mail
import random
from datetime import datetime,time
from django.contrib.auth.hashers import make_password,check_password
from fashion_app.models import *
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from fashion_app.views import *

#==================Index Page view=====================
def seller_index(request):
    return render(request,"seller_index.html")



#==================Register Page view=====================
def seller_register(request):
    if request.method == 'POST' :
        if request.POST["conformpassword"] == request.POST["password"]:
            global seller_user_otp, start_time
            seller_user_otp=random.randint(100000,999999)
            start_time=datetime.now().time()
            subject = 'OTP VERIFICATION PROCESS FOR MAN FASHION'
            message = f'Thanks For Choosing us your OTP is {seller_user_otp}'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [request.POST["email"], ]
            send_mail( subject, message, email_from, recipient_list )
            global seller_temp
            seller_temp={
                "name":request.POST["name"],
                "email":request.POST["email"],
                "password":request.POST["password"],
                "conformpassword":request.POST["conformpassword"]
            }
            return render(request,"seller_otp.html")
        else:
            return render(request,"seller_sign.html",{"msg":"Password And Conform Password not match"})
    else:
        return render(request,"seller_sign.html")



#==================OTP Page view=====================
def seller_otp(request):
    if request.method == "POST" :
        if seller_user_otp==int(request.POST["otp"]):
            seller_end_time=datetime.now().time()
            seller_time_deff=datetime.combine(datetime.today(),seller_end_time) - datetime.combine(datetime.today(),start_time)
            seller_second_deff= seller_time_deff.total_seconds()
            if seller_second_deff < 30:
                Seller_Register.objects.create(
                    seller_name=seller_temp["name"],
                    seller_email=seller_temp["email"],
                    seller_password=make_password(seller_temp["password"]),
                    seller_conformpassword=make_password(seller_temp["conformpassword"])
                )
                return render(request,"seller_index.html",{"msg":seller_temp["name"]})
            else:
                return render(request,"seller_otp.html",{"msg":seller_temp["email"],"msg2":"otp veild in 30 second","recent":True,"cur_email":seller_temp["email"]})
        else:
            return render(request,"seller_otp.html",{"mag":"OTP NOT MATCHED"})
    else:
        return render(request,"seller_sign.html")



# #==================Index Page view=====================
# def seller_resend_email(request,em):
#         global seller_user_otp, start_time
#         seller_user_otp=random.randint(100000,999999)
#         start_time=datetime.now().time()
#         subject = 'OTP VERIFICATION PROCESS FOR MAN FASHION'
#         message = f'Thanks For Choosing us your OTP is {seller_user_otp}'
#         email_from = settings.EMAIL_HOST_USER
#         recipient_list = [request.POST["email"], ]
#         send_mail( subject, message, email_from, recipient_list )
#         return render(request, "seller_otp.html",{"msg":"Otp resend Succesfulkly"})
   


#==================Login Page view=====================
def seller_login(request):
    if request.method == "POST":
        try:
            seller_data=Seller_Register.objects.get(seller_email=request.POST["email"])
            # seller_data=Seller_Register.objects.get(seller_email=request.POST["email"])

            if check_password(request.POST["password"],seller_data.seller_password):
                request.session["email"]=request.POST["email"]
                return render(request,"seller_index.html",{"seller_data":seller_data,"list1":"LISTING","list2":"My Listing","seller_data":seller_data,})
            else:
                return render(request,"seller_login.html",{"msg":"Password Not Match"})
        except:
            return render(request,"seller_login.html",{"msg":"We cannot find an account  with this email address"})

    else:
        return render(request,"seller_login.html")



#==================logout Page view=====================
def seller_logout(reqesut):
    del reqesut.session["email"]
    return render(reqesut,"seller_login.html",{"msg":"Logout Sucsessfully"})


#==================Index Page view=====================
def seller_profile(request):
    if request.method == "POST":
        seller_data=Seller_Register.objects.get(seller_email=request.session["email"])
        try:
            seller_profile_image=request.FILES["propic"]
        except:
            seller_profile_image=seller_data.seller_propic
        if request.POST["newpassword"]:
            if check_password(request.POST["oldpassword"],seller_data.seller_password):
                if request.POST["newconformpassword"]==request.POST["newpassword"]:
                        seller_data.seller_name=request.POST["name"]
                        seller_data.seller_password=make_password(request.POST["newpassword"])
                        seller_data.seller_conformpassword=make_password(request.POST["newconformpassword"])
                        seller_data.seller_propic=seller_profile_image
                        seller_data.save()
                        return render(request,"seller_profile.html",{"seller_data":seller_data,"msg":"Profile Updated Successfully.."})
                else:
                    return render(request,"seller_profile.html",{"seller_data":seller_data,"msg":"New Password and Conform Password Not Match"})
            else:
                return render(request,"seller_profile.html",{"seller_data":seller_data,"msg":"Old Password Is Not Match.."})
        else:
            seller_data.seller_name=request.POST["name"]
            seller_data.seller_propic=seller_profile_image
            seller_data.save()
            return render(request,"seller_profile.html",{"seller_data":seller_data,"msg":"Profile Updated Successfully.."}) 
    else:
        seller_data=Seller_Register.objects.get(seller_email=request.session["email"])
        return render(request,"seller_profile.html",{"seller_data":seller_data}) 




#==================Listing Page view=====================
def seller_listing(request):
    seller_data=Seller_Register.objects.get(seller_email=request.session["email"])

    if request.method == "POST":

        selected_choices = request.POST.getlist('Catalog_Size')
        selected_choices_str = ','.join(selected_choices)

        selected_color=request.POST.getlist('catlog_color')
        selected_color_str=','.join(selected_color)

        try:
            request.FILES["catlog_image"]
            Listing_Catlog.objects.create(
                Catlog_Image=request.FILES["catlog_image"],
                Catlog_Name=request.POST["catlog_name"],
                Catlog_Price=request.POST["catlog_price"],
                Catlog_Sale_Price=request.POST["catlog_sale_price"],
                Catlog_Quntity=request.POST["Catlog_Quntity"],
                Catlog_Catgary=request.POST["Catlog_Catgary"],
                Catlog_Branding=request.POST["Catlog_Branding"],
                Catlog_Tags=request.POST["Catlog_Tags"],
                Catlog_Color=selected_color_str,
                Catlog_Fabric=request.POST["catlog_fabric"],
                Catlog_Discription=request.POST["description"],
                Catlog_Size=selected_choices_str,
                seller=seller_data
            )
        except:
            Listing_Catlog.objects.create(
                Catlog_Name=request.POST["catlog_name"],
                Catlog_Price=request.POST["catlog_price"],
                Catlog_Sale_Price=request.POST["catlog_sale_price"],
                Catlog_Quntity=request.POST["Catlog_Quntity"],
                Catlog_Catgary=request.POST["Catlog_Catgary"],
                Catlog_Branding=request.POST["Catlog_Branding"],
                Catlog_Tags=request.POST["Catlog_Tags"],
                Catlog_Color=selected_color_str,
                Catlog_Fabric=request.POST["catlog_fabric"],
                Catlog_Discription=request.POST["description"], 
                Catlog_Size=selected_choices_str,
                seller=seller_data 
            )
        return render(request,"seller_listing.html",{"msg":"Catlog Upload Successfully..","seller_data":seller_data})
        
    else:
        size=Listing_Catlog.Size
        color=Listing_Catlog.Color
        return render(request,"seller_listing.html",{"seller_data":seller_data,"size":size,"color":color})



#==================All Listing Page view=====================
def all_listing(request): 
    seller_data=Seller_Register.objects.get(seller_email=request.session["email"])
    all_data=Listing_Catlog.objects.filter(seller=seller_data)
    return render(request,"seller_my_listing.html",{"all_data":all_data,"seller_data":seller_data,"msg":"Update is Successfully.."})



#==================Update Listing Page view=====================
def seller_listing_update(request,pk):
    seller_data=Seller_Register.objects.get(seller_email=request.session["email"])
    
    if request.method == 'POST':
        #========Size=======
        selected_choices = request.POST.getlist('Catlog_Size')
        selected_choices_str = ','.join(selected_choices)

        #========Color=======
        selected_color=request.POST.getlist('catlog_color')
        selected_color_str=','.join(selected_color)
        
        one_data=Listing_Catlog.objects.get(id=pk)  
        try:
            catlog_image=request.FILES["catlog_image"]
        except:
            catlog_image=one_data.Catlog_Image

        one_data.Catlog_Image=catlog_image
        one_data.Catlog_Name=request.POST["catlog_name"]
        one_data.Catlog_Price=request.POST["catlog_price"]
        one_data.Catlog_Sale_Price=request.POST["catlog_sale_price"]
        one_data.Catlog_Quntity=request.POST["Catlog_Quntity"]
        one_data.Catlog_Catgary=request.POST["Catlog_Catgary"]
        one_data.Catlog_Branding=request.POST["Catlog_Branding"]
        one_data.Catlog_Tags=request.POST["Catlog_Tags"]
        one_data.Catlog_Color=selected_color_str
        one_data.Catlog_Fabric=request.POST["catlog_fabric"]
        one_data.Catlog_Size=selected_choices_str
        one_data.Catlog_Discription=request.POST["description"]
        one_data.save()
        return all_listing(request)
 
    else:
        color=Listing_Catlog.Color
        size=Listing_Catlog.Size
        one_data=Listing_Catlog.objects.get(id=pk)
        list_size=one_data.Catlog_Size.split(",")
        list_color=one_data.Catlog_Color.split(",")
        return render(request,"seller_update_listing.html",{"one_data":one_data,"seller_data":seller_data,"size":size,"list_size":list_size,"color":color,"list_color":list_color})



#==================Delete Page view=====================
def delete(request,pk):
    one_data=Listing_Catlog.objects.get(id=pk)
    one_data.delete()
    seller_data=Seller_Register.objects.get(seller_email=request.session["email"])
    all_data=Listing_Catlog.objects.filter(seller=seller_data)
    return render(request,"seller_my_listing.html",{"all_data":all_data})



#==================Order Page view=====================
def order(request):
    seller_data=Seller_Register.objects.get(seller_email=request.session["email"]) 
    all_order=Cart.objects.filter(Q(product_id__seller=seller_data) & Q( stetus=False))
    return render(request,"seller_order.html",{"seller_data":seller_data,"all_order":all_order})
    # return render(request,"seller_order.html")


#==================Cancel view=====================
def Cancel(request, pk):
    one_cancel=Cart.objects.get(id=pk)
    one_product=Listing_Catlog.objects.get(id=one_cancel.product_id.id)
    one_product.Catlog_Quntity=int(one_product.Catlog_Quntity)+(one_cancel.qty)
    one_product.save()
    one_cancel.stetus=True
    one_cancel.save()
    return order(request)



#==================Acept Page view=====================
def Accept(request,pk):
    seller_data=Seller_Register.objects.get(seller_email=request.session["email"]) 
    all_order=Cart.objects.get(id=pk)
    return render(request,"seller_acept_order.html",{"seller_data":seller_data,"all_order":all_order})



#==================Order Search Page view=====================
@csrf_exempt
def order_search(request):
    seller_data=Seller_Register.objects.get(seller_email=request.session["email"]) 
    if request.method == 'POST':
        query=request.POST["O_Search"]
        all_order=Cart.objects.filter(Q(Details_id__order_id__icontains=query) | Q(product_id__Catlog_Name__icontains=query))
        if all_order.count() == 0:
            return render(request,"Seller_order.html",{"msg":"Order Not found.."})
        else:
            return render(request,"Seller_order.html",{"seller_data":seller_data,"all_order":all_order})


#==================Payment Page view===================== 
def seller_payment(request):
    seller_data=Seller_Register.objects.get(seller_email=request.session["email"]) 
    all_order=Cart.objects.filter(Q(product_id__seller=seller_data) & Q( stetus=False))
    final_total=0
    for i in all_order:
        final_total=final_total + i.total
    return render(request,"Seller_payment.html",{"seller_data":seller_data,"all_order":all_order,"final_total":final_total})


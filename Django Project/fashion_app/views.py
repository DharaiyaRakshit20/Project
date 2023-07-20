
from django.shortcuts import render
import razorpay
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest
from django.shortcuts import render
from .models import *
from django.conf import settings
from django.core.mail import send_mail
import random
from datetime import datetime,time
from django.contrib.auth.hashers import make_password,check_password
from seller_app.models import *
from django.db.models import Q
from django.http import HttpResponse
import razorpay
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
import requests


#==================Login required custom=====================
def login_required_custom(view_func):
    def wrapper(request, *args, **kwargs):
        try:
            request.session["email"]
        except:
            return redirect("Error")
        return view_func(request, *args, **kwargs)
    return wrapper


#==================Error view=====================
def Error(request):
    return render(request,"sign.html",{"msg":"Plese Register First.."}) 
            

#==================Home Page view=====================
def home(request):
    try:   
        data=Register.objects.get(email=request.session["email"])
        all_num=Cart.objects.filter(Q(buyer_id=data.id) & Q( stetus=True)).count()
        final_total=final(request) 
        return render(request,"index.html",{"data":data,"all_num":all_num,"final_total":final_total})
    except:
        return render(request,"index.html")


#==================Register Page view=====================
def register(request):
    if request.method == 'POST' :
        api_key = 'jr3O1p9Q.Vduo2dduK8kQtHGOVWbRki3tVygJ30dp' # Generated in your User Profile it shows at the top in a green bar once
        team_slug = "rakshitdharaiya" # when you sign up you have a team, its in the URL then use that
        email_address = request.POST["email"] # the test email


        response = requests.post(
            "https://app.mailvalidation.io/a/" + team_slug + "/validate/api/validate/",
            json={'email': email_address},
            headers={
                    'content-type': 'application/json',
                    'accept': 'application/json',
                    'Authorization': 'Api-Key ' + api_key,
                    },
        )

        valid = response.json()['is_valid']

        if valid:
            if request.POST["conformpassword"] == request.POST["password"]:
                global user_otp, start_time
                user_otp=random.randint(100000,999999)
                start_time=datetime.now().time()
                subject = 'OTP VERIFICATION PROCESS FOR MAN FASHION'
                message = f'Thanks For Choosing us your OTP is {user_otp}'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [request.POST["email"], ]
                send_mail( subject, message, email_from, recipient_list )
                global temp
                temp={
                    "name":request.POST["name"],
                    "email":request.POST["email"],
                    "password":request.POST["password"],
                    "conformpassword":request.POST["conformpassword"]
                }
                return render(request,"otp.html")
            else:
                return render(request,"sign.html",{"msg":"Password And Conform Password not match"})
        else:
            return render(request,"sign.html",{"msg":"Invalid Email"})
        
    else:
        return render(request,"sign.html")


#==================OTP Page view=====================
def otp(request):
    if request.method == "POST" :
        if user_otp==int(request.POST["otp"]):
            end_time=datetime.now().time()
            time_deff=datetime.combine(datetime.today(),end_time) - datetime.combine(datetime.today(),start_time)
            second_deff= time_deff.total_seconds()
            if second_deff < 30:
                Register.objects.create(
                    name=temp["name"],
                    email=temp["email"],
                    password=make_password(temp["password"]),
                    conformpassword=make_password(temp["conformpassword"])
                )
                return render(request,"index.html",{"msg":temp["name"]})
            else:
                return render(request,"otp.html",{"msg":temp["email"],"msg2":"otp veild in 30 second","recent":True,"cur_email":temp["email"]})
        else:
            return render(request,"otp.html",{"mag":"OTP NOT MATCHED"})
    else:
        return render(request,"sign.html")


#==================Index Page view=====================
# def resend_email(request,em):
#         global user_otp, start_time
#         user_otp=random.randint(100000,999999)
#         start_time=datetime.now().time()
#         subject = 'OTP VERIFICATION PROCESS FOR MAN FASHION'
#         message = f'Thanks For Choosing us your OTP is {user_otp}'
#         email_from = settings.EMAIL_HOST_USER
#         recipient_list = [request.POST["email"], ]
#         send_mail( subject, message, email_from, recipient_list )
#         return render(request, "otp.html",{"msg":"Otp resend Succesfulkly"})
   


#==================Login Page view=====================
def login(request):
    if request.method == "POST":
        try:
            data=Register.objects.get(email=request.POST["email"])
            if check_password(request.POST["password"],data.password):
                request.session["email"]=request.POST["email"]
                return render(request,"index.html",{"data":data})
            else:
                return render(request,"login.html",{"msg":"Password Not Match"})
        except:
            return render(request,"login.html",{"msg":"We cannot find an account  with this email address"})

    else:
        return render(request,"login.html")


#==================Logout Page view=====================
def logout(reqesut):
    del reqesut.session["email"]
    return render(reqesut,"login.html",{"msg":"Logout Sucsessfully"})


#==================Profile Page view=====================
@login_required_custom
def profile(request):
    if request.method == "POST":
        data=Register.objects.get(email=request.session["email"])
        all_num=Cart.objects.filter(Q(buyer_id=data.id) & Q( stetus=True)).count()
        final_total=final(request)
        try:
            profile_image=request.FILES["propic"]
        except:
            profile_image=data.propic
        if request.POST["newpassword"]:
            if check_password(request.POST["oldpassword"],data.password):
                if request.POST["newconformpassword"]==request.POST["newpassword"]:
                        data.name=request.POST["name"]
                        data.password=make_password(request.POST["newpassword"])
                        data.conformpassword=make_password(request.POST["newconformpassword"])
                        data.propic=profile_image
                        data.save()
                        return render(request,"profile.html",{"data":data,"msg":"Profile Updated Successfully.."})
                else:
                    return render(request,"profile.html",{"data":data,"msg":"New Password and Conform Password Not Match"})
            else:
                return render(request,"profile.html",{"data":data,"msg":"Old Password Is Not Match.."})
        else:
            data.name=request.POST["name"]
            data.propic=profile_image
            data.save()
            return render(request,"profile.html",{"data":data,"msg":"Profile Updated Successfully.."}) 
    else:
        data=Register.objects.get(email=request.session["email"])
        return render(request,"profile.html",{"data":data,"all_num":all_num,"final_total":final_total}) 


#==================Shop Page view====================
@login_required_custom
def shop(request):
    data=Register.objects.get(email=request.session["email"])
    all_num=Cart.objects.filter(Q(buyer_id=data.id) & Q( stetus=True)).count()
    final_total=final(request)
    all_data=Listing_Catlog.objects.all()

    return render(request,"shop.html",{"all_data":all_data,"data":data,"all_num":all_num,"final_total":final_total})



#==================Shop Details Page view=====================
def shop_details(request,pk):
    data=Register.objects.get(email=request.session["email"])
    all_num=Cart.objects.filter(Q(buyer_id=data.id) & Q( stetus=True)).count()
    final_total=final(request)
    one_data=Listing_Catlog.objects.get(id=pk)
    return render(request,"shop-details.html",{"data":data,"final_total":final_total,"all_num":all_num,"one_data":one_data,"sizes":one_data.Catlog_Size.split(","),"colors":one_data.Catlog_Color.split(",")})



#==================Shipping Cart Page view=====================
def shopping_cart(request,pk):
    data=Register.objects.get(email=request.session["email"])
    try:
        product=Listing_Catlog.objects.get(id=pk)  
        exists_data=Cart.objects.get( Q(product_id=pk) & Q(buyer_id=data.id) & Q( stetus=True))
        exists_data.qty+=1
        exists_data.total=exists_data.qty * exists_data.product_id.Catlog_Price
        exists_data.save()
        # return cart(request)
        return redirect('cart')
    except:
        product=Listing_Catlog.objects.get(id=pk)  
        Cart.objects.create(
            product_id=product,
            buyer_id=data,
            qty=1,
            total=product.Catlog_Price,
            product_color=request.POST.getlist("color"),
            product_size=request.POST.getlist("size")  
        )
        return cart(request)


#==================Cart Page view=====================
@login_required_custom
def cart(request):
    data=Register.objects.get(email=request.session["email"])
    all_num=Cart.objects.filter(Q(buyer_id=data.id) & Q( stetus=True)).count()
    final_total=final(request)
    all_cart=Cart.objects.filter(Q(buyer_id=data.id) & Q( stetus=True))
    final_total=0
    for i in all_cart:
        final_total=final_total+i.total
    return render(request,"shopping-cart.html",{"all_cart":all_cart,"final_total":final_total,"data":data,"all_num":all_num})



#==================Delete Cart view=====================
def delete_cart(request,pk):
    data=Register.objects.get(email=request.session["email"])
    cart_data=Cart.objects.get(id=pk)
    cart_data.delete()
    return cart(request)



#==================Update Cart  view=====================
def update_cart(request):
    data=Register.objects.get(email=request.session["email"])
    if request.method == "POST":
        l1=request.POST.getlist("uqty")
        all_cart=Cart.objects.filter(Q(buyer_id=data.id) & Q( stetus=True))
        for i,j in zip(all_cart,l1) :
            i.qty=j
            i.total=int(j)*i.product_id.Catlog_Price
            i.save()
        return cart(request)    
    else:
        return cart(request)    


#==================Final view=====================
def final(request):
    # all_num=Cart.objects.filter(Q(buyer_id=data.id) & Q( stetus=True)).count()
    data=Register.objects.get(email=request.session["email"])
    all_cart=Cart.objects.filter(Q(buyer_id=data.id) & Q( stetus=True))
    final_total=0
    for i in all_cart:
        final_total=final_total+i.total
    return final_total


#==================Checkout Page view=====================
@login_required_custom
def checkout(request):
    data=Register.objects.get(email=request.session["email"])
    all_num=Cart.objects.filter(Q(buyer_id=data.id) & Q( stetus=True)).count()
    all_cart=Cart.objects.filter(Q(buyer_id=data.id) & Q( stetus=True))
    # final_total=0
    # for i in all_cart:
    #     final_total=final_total+i.total
    final_total=final(request)
    return render(request,"checkout.html",{"final_total":final_total,"all_cart":all_cart,"data":data,"all_num":all_num})



#==================Search Page view=====================
def search(request):
    all_num=Cart.objects.filter(Q(buyer_id=data.id) & Q( stetus=True)).count()
    final_total=final(request)
    data=Register.objects.get(email=request.session["email"])
    if request.method == "POST":
        query=request.POST["search"]
        all_data=Listing_Catlog.objects.filter(Q(Catlog_Name__icontains=query) | Q(Catlog_Discription__icontains=query))
        if all_data.count()==0:
             return render(request,"shop.html",{"msg":"Product Not found"})
        else:
            return render(request,"shop.html",{"all_data": all_data,"data":data,"all_num":all_num,"final_total":final_total}) 


#==================Checkout Details Page view=====================
@csrf_exempt
def checkout_details(request):
    data=Register.objects.get(email=request.session["email"])
    all_num=Cart.objects.filter(Q(buyer_id=data.id) & Q( stetus=True)).count()
    final_total=final(request)
    all_cart=Cart.objects.filter(Q(buyer_id=data.id) & Q( stetus=True))

    l1=["a","x","q","e","t","_","1","5","7","3"]
    a=random.choices(l1,k=10)
    order_id_="".join(a)
    if request.method == "POST":
        try:
             one_order=Details.objects.get(buyer_id=data)
        except:
            Details.objects.create(
                firstname=request.POST["fristname"],
                lastname=request.POST["lastname"],
                country=request.POST["country"],
                address=request.POST["address"],
                second_address=request.POST["second_address"],
                city=request.POST["city"],
                state=request.POST["state"],
                postcode=request.POST["postcode"],
                phone=request.POST["phone"],
                email=request.POST["email"],
                order_id=order_id_,
                buyer_id=data
            )
        one_order=Details.objects.get(buyer_id=data)
        for i in all_cart:
             i.Details_id=one_order
             i.save()
        return render(request,"Payment.html",{"data":data,"all_cart":all_cart,"all_num":all_num,"final_total":final_total})
    else:
         return render(request,"checkout.html",{"data":data,"all_num":all_num,"final_total":final_total})


#==================All Delete Page view=====================
def all_delete(request):
    data=Register.objects.get(email=request.session["email"])
    all_cart=Cart.objects.filter(Q(buyer_id=data.id) & Q( stetus=True))
    for i in all_cart:
        one_data=Listing_Catlog.objects.get(id=i.product_id.id)
        one_data.Catlog_Quntity=int(one_data.Catlog_Quntity)-i.qty
        # one_cart=Cart.objects.get(id=i.id)
        i.stetus=False
        i.save()
        one_data.save()
    # all_cart.delete()
    return shop(request)


#==================Payment view=====================
@csrf_exempt
def payment(request):
    return all_delete(request)


#==================Categories view=====================
def Categories(request,pk):
    data=Register.objects.get(email=request.session["email"])
    all_num=Cart.objects.filter(Q(buyer_id=data.id) & Q( stetus=True)).count()
    final_total=final(request)
    all_data=Listing_Catlog.objects.filter(Catlog_Catgary=pk)
    # c=all_data.count()
    return render(request,"shop.html",{"all_data":all_data,"all_num":all_num,"final_total":final_total,"data":data}) 


#==================Categories_B view=====================
def Categories_B(request,pk):
    data=Register.objects.get(email=request.session["email"])
    all_num=Cart.objects.filter(Q(buyer_id=data.id) & Q( stetus=True)).count()
    final_total=final(request)
    all_data=Listing_Catlog.objects.filter(Catlog_Branding=pk)
    return render(request,"shop.html",{"all_data":all_data,"all_num":all_num,"final_total":final_total,"data":data})    


#==================Categories_P view=====================
def Categories_P(request,pk):
    data=Register.objects.get(email=request.session["email"])
    all_num=Cart.objects.filter(Q(buyer_id=data.id) & Q( stetus=True)).count()
    final_total=final(request)
    l1=pk.split("-")
    all_data=Listing_Catlog.objects.filter(Q(Catlog_Price__gt=(int(l1[0])))&Q(Catlog_Price__lt=int(l1[1])))
    return render(request,"shop.html",{"all_data":all_data,"all_num":all_num,"final_total":final_total,"data":data})    
     


#==================Categories_S view=====================
def Categories_S(request,pk):
    data=Register.objects.get(email=request.session["email"])
    all_num=Cart.objects.filter(Q(buyer_id=data.id) & Q( stetus=True)).count()
    final_total=final(request)
    all_data=Listing_Catlog.objects.filter(Catlog_Size=pk)
    return render(request,"shop.html",{"all_data":all_data,"all_num":all_num,"final_total":final_total,"data":data}) 


#==================Categories_C view=====================
def Categories_C(request,pk):
    data=Register.objects.get(email=request.session["email"])
    all_num=Cart.objects.filter(Q(buyer_id=data.id) & Q( stetus=True)).count()
    final_total=final(request)
    all_data=Listing_Catlog.objects.filter(Catlog_Color=pk)
    return render(request,"shop.html",{"all_data":all_data,"all_num":all_num,"final_total":final_total,"data":data}) 


#==================Categories_T view=====================
def Categories_T(request,pk):
    data=Register.objects.get(email=request.session["email"])
    all_num=Cart.objects.filter(Q(buyer_id=data.id) & Q( stetus=True)).count()
    final_total=final(request)
    all_data=Listing_Catlog.objects.filter(Catlog_Tags=pk)
    return render(request,"shop.html",{"all_data":all_data,"all_num":all_num,"final_total":final_total,"data":data}) 



#==================My Order view=====================
def my_order(request):
    data=Register.objects.get(email=request.session["email"])
    all_num=Cart.objects.filter(Q(buyer_id=data.id) & Q( stetus=True)).count()
    final_total=final(request)
    all_cart=Cart.objects.filter(Q(buyer_id=data.id) & Q( stetus=False))
    return render(request,"order.html",{"data":data,"all_num":all_num,"final_total":final_total,"all_cart":all_cart})


#==================Contact view=====================
def contact(request):
    data=Register.objects.get(email=request.session["email"])
    all_num=Cart.objects.filter(Q(buyer_id=data.id) & Q( stetus=True)).count()
    return render(request,"contact.html",{"data":data,"all_num":all_num})


#==================About Us view=====================
def about_us(request):
    all_num=Cart.objects.filter(Q(buyer_id=data.id) & Q( stetus=True)).count()
    data=Register.objects.get(email=request.session["email"])
    return render(request,"about.html",{"data":data,"all_num":all_num})


#==================Blog view=====================
def blog(request):
    all_num=Cart.objects.filter(Q(buyer_id=data.id) & Q( stetus=True)).count()
    data=Register.objects.get(email=request.session["email"])
    return render(request,"blog-details.html",{"data":data,"all_num":all_num})


#===============Payment Razorpay===============


# authorize razorpay client with API Keys.
razorpay_client = razorpay.Client(
	auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))



# we need to csrf_exempt this url as
# POST request will be made by Razorpay
# and it won't have the csrf token.
@csrf_exempt
def paymenthandler(request):

	# only accept POST request.
	if request.method == "POST":
		try:
		
			# get the required parameters from post request.
			payment_id = request.POST.get('razorpay_payment_id', '')
			razorpay_order_id = request.POST.get('razorpay_order_id', '')
			signature = request.POST.get('razorpay_signature', '')
			params_dict = {
				'razorpay_order_id': razorpay_order_id,
				'razorpay_payment_id': payment_id,
				'razorpay_signature': signature
			}

			# verify the payment signature.
			result = razorpay_client.utility.verify_payment_signature(
				params_dict)
			if result is not None:
				amount = 20000 # Rs. 200
				try:

					# capture the payemt
					razorpay_client.payment.capture(payment_id, amount)

					# render success page on successful caputre of payment
					return render(request,'checkout.html',{"msg":"Your Payment Is Successfully.."})
				except:

					# if there is an error while capturing payment.
					return render(request,"checkout.html",{"msg":"Your Payment Is Faild.."})

			else:

				# if signature verification fails.
				return render(request, 'paymentfail.html')
		except:

			# if we don't find the required parameters in POST data
			return all_delete(request)
	else:
	# if other than POST request is made.
		return render(request,"checkout.html",{"msg":"Your Payment Is Faild.."}) 
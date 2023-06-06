from tkinter import *
import random
root=Tk()

root.geometry("1280x700")
# root.maxsize(width=1280,height=700)
# root.minsize(width=1280,height=700)
root.title("PATEL PAVBHAJI")

#======================Variable========================

bg_color = "black"
fg_color = "white"
lbl_color = 'white'

cus_name = StringVar()
c_phone = StringVar()
#==For Generating Random Bill Numbers==
x = random.randint(1000,9999)
c_bill_no = StringVar()
#==Seting Value to variable==
c_bill_no.set(str(x))

Net_Total=IntVar()
total_pavbhaji_prices=IntVar()
total_greenbhaji_prices=IntVar()
total_other_prices=IntVar()
oil_bhaji = IntVar()
butter_bhaji = IntVar()
chezz_bhaji = IntVar()
chezz_butter_bhaji = IntVar()
jain_bhaji = IntVar()
chezz_jain_bhaji = IntVar()
green_bhaji = IntVar()
butter_green_bhaji = IntVar()
chezz_green_bhaji = IntVar()
chezz_butter_green = IntVar()
butter_jain_bhaji = IntVar()
butter_chezz_bhaji = IntVar()
butter_milk = IntVar()
papad = IntVar()
green_chatni = IntVar()
oil_pav = IntVar()
butter_pav = IntVar()
rosted_papad = IntVar()
total_bhaji = StringVar()
total_green_bhaji = StringVar()
total_other = StringVar()
tax_other = StringVar()
tax_bhaji = StringVar()
tax_green_bhaji = StringVar()

def total():
#=================Total Cosmetics Prices=========================
    global total_pavbhaji_prices,total_bhaji,tax_bhaji
    total_pavbhaji_prices = (
        (oil_bhaji.get() * 100)+
        (butter_bhaji.get() * 110)+
        (chezz_bhaji.get() * 140)+
        (chezz_butter_bhaji.get() * 160)+
        (jain_bhaji.get() * 100)+
        (butter_jain_bhaji.get() * 110)
    )
    total_bhaji.set("Rs. "+str(total_pavbhaji_prices))
    print(total_pavbhaji_prices)
    tax_bhaji.set("Rs. "+str(round(total_pavbhaji_prices * 0.05)))
#=================Total Grocery Prices===========================
    global total_greenbhaji_prices,total_green_bhaji,tax_green_bhaji
    total_greenbhaji_prices = (
        (green_bhaji.get() * 110)+
        (butter_green_bhaji.get() * 130)+
        (chezz_green_bhaji.get() * 150)+
        (chezz_butter_green.get() *170)+
        (chezz_jain_bhaji.get() * 140)+
        (butter_chezz_bhaji.get() * 160)

    )
    total_green_bhaji.set("Rs. "+str(total_greenbhaji_prices))
    tax_green_bhaji.set("Rs. "+str(round(total_greenbhaji_prices*0.05)))
     
#======================Total Other Prices========================
    global total_other_prices,total_other,tax_other
    total_other_prices = (
        (butter_milk.get() * 20)+
        (oil_pav.get() * 5)+
        (butter_pav.get() * 10)+
        (green_chatni.get() * 60)+
        (papad.get() * 10)+
        (rosted_papad.get() * 30)
    )
    total_other.set("Rs. "+str(total_other_prices))
    tax_other.set("Rs. "+str(round(total_other_prices*0.05)))

#===================Function For Text Area====================
def welcome_soft():
    txt.delete('1.0',END)
    txt.insert(END,"           Welcome To Patel PavBhaji\n")
    txt.insert(END,f"\nBill No. : {str(c_bill_no.get())}")
    txt.insert(END,f"\nCustomer Name : {str(cus_name.get())}")
    txt.insert(END,f"\nPhone No. : {str(c_phone.get())}")
    txt.insert(END,"\n===========================================")
    txt.insert(END,"\nProduct             Qty             Price")
    txt.insert(END,"\n===========================================")


#==========Add Product name , qty and price to bill area===============
def bill_area():
    welcome_soft()
    if oil_bhaji.get() != 0:
        txt.insert(END,f"\nOil Bhaji            {oil_bhaji.get()}                {oil_bhaji.get() * 100}")
    if butter_bhaji.get() != 0:
        txt.insert(END,f"\nButter Bhaji         {butter_bhaji.get()}                {butter_bhaji.get() * 110}")
    if chezz_bhaji.get() != 0:
        txt.insert(END,f"\nChezz Bhaji          {chezz_bhaji.get()}                {chezz_bhaji.get() * 140}")
    if chezz_butter_bhaji.get() != 0:
        txt.insert(END,f"\nChezz Butter Bhaji   {chezz_butter_bhaji.get()}                {chezz_butter_bhaji.get() * 160}")
    if jain_bhaji.get() != 0:
        txt.insert(END,f"\nJain Bhaji           {jain_bhaji.get()}                {jain_bhaji.get() * 100}")
    if butter_jain_bhaji.get() != 0:
        txt.insert(END,f"\nButter jain Bhaji    {butter_jain_bhaji.get()}                {butter_jain_bhaji.get() * 110}")
    if green_bhaji.get() != 0:
        txt.insert(END,f"\nGreen Bhaji          {green_bhaji.get()}                {green_bhaji.get() * 110}")
    if butter_green_bhaji.get() != 0:
        txt.insert(END,f"\nButter Green Bhaji   {butter_green_bhaji.get()}                {butter_green_bhaji.get() * 130}")
    if chezz_green_bhaji.get() != 0:
        txt.insert(END,f"\nChezz Green Bhaji    {chezz_green_bhaji.get()}                {chezz_green_bhaji.get() * 150}")
    if chezz_butter_green.get() != 0:
        txt.insert(END,f"\nChezz Butter Green   {chezz_butter_green.get()}                {chezz_butter_green.get() * 170}")
    if chezz_jain_bhaji.get() != 0:
        txt.insert(END,f"\nChezz Jain Bhaji     {chezz_jain_bhaji.get()}                {chezz_jain_bhaji.get() * 140}")
    if butter_chezz_bhaji.get() != 0:
        txt.insert(END,f"\nChezz Butter jain    {butter_chezz_bhaji.get()}                {butter_chezz_bhaji.get() * 160}")
    if butter_milk.get() != 0:
        txt.insert(END,f"\nButter Milk          {butter_milk.get()}                {butter_milk.get() * 20}")
    if oil_pav.get() != 0:
        txt.insert(END,f"\nOil Pav(1Pis)        {oil_pav.get()}                {oil_pav.get() * 5}")
    if butter_pav.get() != 0:
        txt.insert(END,f"\nButter Pav(1pis)     {butter_pav.get()}                {butter_pav.get() * 10}")
    if green_chatni.get() != 0:
        txt.insert(END,f"\nGreen Chatni         {green_chatni.get()}                {green_chatni.get() * 60}")
    if papad.get() != 0:
        txt.insert(END,f"\nPapad                {papad.get()}                {papad.get() * 10}")
    if rosted_papad.get() != 0:
        txt.insert(END,f"\nMasala Papad         {rosted_papad.get()}                {rosted_papad.get() * 30}")
    txt.insert(END,"\n===========================================")
    txt.insert(END,f"\n                           Total : {total_pavbhaji_prices+total_greenbhaji_prices+total_other_prices+(total_pavbhaji_prices*0.05)+(total_greenbhaji_prices*0.05)+(total_other_prices*0.05)}")


def clear():
    txt.delete('1.0',END)

def exit():
    root.destroy()



#============Title Fream===========
title=Label(root,text="PATEL PAVBHAJI",bd=12,bg=bg_color,fg=fg_color,relief="groove",font=("time new romen",30,"bold"),pady=13)
title.pack(fill=X)

#===========Customer Fream==============
F1=LabelFrame(text="Customer Ditails",font=("time new roman",12,"bold"),fg="gold",bg=bg_color,relief="groove",bd=10)
F1.place(x = 0,y = 90,relwidth= 1 )

#===============Customer Name===========#
cname_lbl=Label(F1,text="Customer Name ",bg=bg_color,fg=fg_color,font=("time new roman",15,"bold")).grid(row=0,column=0,padx=30,pady=5)
cname_en=Entry(F1,bd=8,relief="groove",textvariable=cus_name)
cname_en.grid(row=0,column=1,ipadx=40,ipady=4,pady=5)

#==============Customer Phone===========
cphone_lbl=Label(F1,text="Phone No.",bg=bg_color,fg=fg_color,font=("time new roman",15,"bold")).grid(row=0,column=2,padx=30)
cphone_en=Entry(F1,bd=8,relief="groove",textvariable=c_phone)
cphone_en.grid(row=0,column=3,ipadx=40,ipady=4,pady=5)

#=============Bill No==============
cbill_lbl=Label(F1,text="Bill No.",bg=bg_color,fg=fg_color,font=("time new roman",15,"bold")).grid(row=0,column=4,padx=30)
cbill_en=Entry(F1,bd=8,relief="groove",textvariable=c_bill_no)
cbill_en.grid(row=0,column=5,ipadx=40,ipady=4,pady=5)

#============Enter Button=========
cEnter=Button(F1,text="Enter",bg=bg_color,fg=fg_color,font=("time new roman",15,"bold"))
cEnter.grid(row=0,column=6,ipadx=45,padx=100,ipady=5,pady=5,)

#==========Costmetic ===============
F2=LabelFrame(text="PAVBHAJI",bg=bg_color,fg="gold",font=("time new roman",12,"bold"),relief="groove",bd=10)
F2.place(x=0,y=180,width=385,height=380)

#===========Bath Shop==============
bath_lbl=Label(F2,text="OIL BHAJI",font=("time new roman",10,"bold"),bg=bg_color,fg=fg_color)
bath_lbl.grid(row=0,column=0,padx=30,pady=18)
bath_en=Entry(F2,bd=8,relief="groove",textvariable=oil_bhaji)
bath_en.grid(row=0,column=1,ipadx=24,ipady=4)

#============Face cream=================
face_lbl=Label(F2,text="BUTTER BHAJI",font=("time new roman",10,"bold"),bg=bg_color,fg=fg_color)
face_lbl.grid(row=1,column=0,padx=10,pady=18)
face_en=Entry(F2,bd=8,relief="groove",textvariable=butter_bhaji)
face_en.grid(row=1,column=1,ipadx=24,ipady=4)

#============Face Wash===============
wash_lbl=Label(F2,text="CHEZZ BHAJI",font=("time new roman",10,"bold"),bg=bg_color,fg=fg_color)
wash_lbl.grid(row=3,column=0,padx=10,pady=18)
wash_en=Entry(F2,bd=8,relief="groove",textvariable=chezz_bhaji)
wash_en.grid(row=3,column=1,ipadx=24,ipady=4)

#=============Hair Spary==============
hair_lbl=Label(F2,text="CHEZZ BUTTER BHAJI",font=("time new roman",10,"bold"),bg=bg_color,fg=fg_color)
hair_lbl.grid(row=4,column=0,padx=10,pady=18)
hair_en=Entry(F2,bd=8,relief="groove",textvariable=chezz_butter_bhaji)
hair_en.grid(row=4,column=1,ipadx=24,ipady=4)

#============body lotion==============
body_lbl=Label(F2,text="JAIN BHAJI",fg=fg_color,bg=bg_color,font=("time new roman",10,"bold"))
body_lbl.grid(row=5,column=0,padx=10,pady=18)
body_en=Entry(F2,bd=8,relief="groove",textvariable=jain_bhaji)
body_en.grid(row=5,column=1,ipadx=24,ipady=4)

#============body lotion==============
body_lbl=Label(F2,text="BUTTER JAIN BHAJI",fg=fg_color,bg=bg_color,font=("time new roman",10,"bold"))
body_lbl.grid(row=6,column=0,padx=10,pady=18)
body_en=Entry(F2,bd=8,relief="groove",textvariable=butter_jain_bhaji)
body_en.grid(row=6,column=1,ipadx=24,ipady=4)

#==============Grosary Fream==============
F3=LabelFrame(text="GREEN PAVBHAJI",bg=bg_color,fg="gold",font=("time new roman",12,"bold"),relief="groove",bd=10)
F3.place(x=385,y=180,width=386,height=380)

#===============Rice===================
rice_lbl=Label(F3,text="GREEN BHAJI",font=("time new roman",10,"bold"),bg=bg_color,fg=fg_color)
rice_lbl.grid(row=0,column=0,padx=10,pady=18)
rice_en=Entry(F3,bd=8,relief="groove",textvariable=green_bhaji)
rice_en.grid(row=0,column=1,ipadx=10,ipady=4)
#=================Food oil===================
Foodoil_lbl=Label(F3,text="BUTTER GREEN BHAJI",font=("time new roman",10,"bold"),bg=bg_color,fg=fg_color)
Foodoil_lbl.grid(row=1,column=0,padx=10,pady=18)
Foodoil_en=Entry(F3,bd=8,relief="groove",textvariable=butter_green_bhaji)
Foodoil_en.grid(row=1,column=1,ipadx=10,ipady=4)

#====================Daal====================
daal_lbl=Label(F3,text="CHEZZ BUTTEER 'G' BHAJI",font=("time new roman",10,"bold"),bg=bg_color,fg=fg_color)
daal_lbl.grid(row=3,column=0,padx=10,pady=18)
daal_en=Entry(F3,bd=8,relief="groove",textvariable=chezz_butter_green)
daal_en.grid(row=3,column=1,ipadx=10,ipady=4)

#=====================Wheat===================
wheat_lbl=Label(F3,text="CHEZZ GREEN BHAJI",font=("time new roman",10,"bold"),bg=bg_color,fg=fg_color)
wheat_lbl.grid(row=4,column=0,padx=10,pady=18)
wheat_en=Entry(F3,bd=8,relief="groove",textvariable=chezz_green_bhaji)
wheat_en.grid(row=4,column=1,ipadx=10,ipady=4)

#===================Sugar======================
sugar_lbl=Label(F3,text="CHEZZ JAIN BHAJI",fg=fg_color,bg=bg_color,font=("time new roman",10,"bold"))
sugar_lbl.grid(row=5,column=0,padx=10,pady=18)
sugar_en=Entry(F3,bd=8,relief="groove",textvariable=chezz_jain_bhaji)
sugar_en.grid(row=5,column=1,ipadx=10,ipady=4)

#===================Sugar======================
sugar_lbl=Label(F3,text="BUTTER CHEEZ JAIN",fg=fg_color,bg=bg_color,font=("time new roman",10,"bold"))
sugar_lbl.grid(row=6,column=0,padx=10,pady=18)
sugar_en=Entry(F3,bd=8,relief="groove",textvariable=butter_chezz_bhaji)
sugar_en.grid(row=6,column=1,ipadx=10,ipady=4)

#==================Other========================
F4=LabelFrame(text="OTHER ITEM",bg=bg_color,fg="gold",font=("time new roman",12,"bold"),relief="groove",bd=10)
F4.place(x=771,y=180,width=385,height=380)

#=====================Maza====================
maza_lbl=Label(F4,text="BUTTER MILK",font=("time new roman",10,"bold"),bg=bg_color,fg=fg_color)
maza_lbl.grid(row=0,column=0,padx=10,pady=18)
maza_en=Entry(F4,bd=8,relief="groove",textvariable=butter_milk)
maza_en.grid(row=0,column=1,ipadx=25,ipady=4)

#====================coke=======================
coke_lbl=Label(F4,text="OIL PAV(1 PIS)",font=("time new roman",10,"bold"),bg=bg_color,fg=fg_color)
coke_lbl.grid(row=1,column=0,padx=10,pady=18)
coke_en=Entry(F4,bd=8,relief="groove",textvariable=oil_pav)
coke_en.grid(row=1,column=1,ipadx=25,ipady=4)

#=====================fruti=======================
fruti_lbl=Label(F4,text="BUTTER PAV(1 PIS)",font=("time new roman",10,"bold"),bg=bg_color,fg=fg_color)
fruti_lbl.grid(row=3,column=0,padx=10,pady=18)
fruti_en=Entry(F4,bd=8,relief="groove",textvariable=butter_pav)
fruti_en.grid(row=3,column=1,ipadx=25,ipady=4)

#=========================nimkos========================
nimko_lbl=Label(F4,text="GREEN CHATNI",font=("time new roman",10,"bold"),bg=bg_color,fg=fg_color)
nimko_lbl.grid(row=4,column=0,padx=10,pady=18)
nimko_en=Entry(F4,bd=8,relief="groove",textvariable=green_chatni)
nimko_en.grid(row=4,column=1,ipadx=25,ipady=4)

#==================biscuits=============================
biscutis_lbl=Label(F4,text="PAPAD",fg=fg_color,bg=bg_color,font=("time new roman",10,"bold"))
biscutis_lbl.grid(row=5,column=0,padx=10,pady=18)
biscutis_en=Entry(F4,bd=8,relief="groove",textvariable=papad)
biscutis_en.grid(row=5,column=1,ipadx=25,ipady=4)

#===================Sugar======================
sugar_lbl=Label(F4,text="ROSTED PAPAD",fg=fg_color,bg=bg_color,font=("time new roman",10,"bold"))
sugar_lbl.grid(row=6,column=0,padx=10,pady=18)
sugar_en=Entry(F4,bd=8,relief="groove",textvariable=rosted_papad)
sugar_en.grid(row=6,column=1,ipadx=25,ipady=4)

#===================bill Area=========================
F5=Frame(root,bd=8,relief="groove")
F5.place(x=1154,y=180,width=386,height=380)
bill_titel=Label(F5,text="Bill Area",font=("Lucida",15,"bold"),bd=7,relief="groove")
bill_titel.pack(fill=X)

#====================Scroll bar in bill area=================
scroll_y=Scrollbar(F5,orient="vertical")
txt=Text(F5,yscrollcommand=scroll_y.set)
scroll_y.pack(side=RIGHT,fill=Y)
scroll_y.config(command=txt.yview)
txt.pack(fill=BOTH,expand=1)

#====================bill manu========================
F6=LabelFrame(root,text="Bill Manu",bg=bg_color,fg="gold",relief="groove",bd=10,font=("time new roman",12,"bold"))
F6.place(x=0,y=560,relwidth=1,height=232)

#======================cosmatics====================
cosmatics_lbl=Label(F6,text="Total PAVBHAJI",bg=bg_color,fg=lbl_color,font=("time new roman",15,"bold"))
cosmatics_lbl.grid(row=0,column=0,padx=18,pady=15)
cosmatics_en=Entry(F6,bd=8,relief="groove",textvariable=total_bhaji)
cosmatics_en.grid(row=0,column=1,ipadx=12,ipady=8)

#======================Total Grosary=========================
grosary_lbl=Label(F6,text="Total GREEN BHAJI",bg=bg_color,fg=lbl_color,font=("time new roman",15,"bold"))
grosary_lbl.grid(row=1,column=0,padx=18,pady=15)
grosary_en=Entry(F6,bd=8,relief="groove",textvariable=total_green_bhaji)
grosary_en.grid(row=1,column=1,ipadx=12,ipady=8)

#===================total Other=========================
othetr_lbl=Label(F6,text="Total OTHER",bg=bg_color,fg=lbl_color,font=("time new roman",15,"bold"))
othetr_lbl.grid(row=2,column=0,padx=18,pady=15)
other_en=Entry(F6,bd=8,relief="groove",textvariable=total_other)
other_en.grid(row=2,column=1,ipadx=12,ipady=8)

#=======================cosmatics tax=======================
ctax_lbl=Label(F6,text="PAVBHAJI TAX",bg=bg_color,fg=lbl_color,font=("time new roman",15,"bold"))
ctax_lbl.grid(row=0,column=2,padx=18,pady=15)
ctax_en=Entry(F6,bd=8,relief="groove",textvariable=tax_bhaji)
ctax_en.grid(row=0,column=3,ipadx=12,ipady=8)

#=======================grosary tax=========================
gtax_lbl=Label(F6,text="GREEN BHAJI TAX",bg=bg_color,fg=lbl_color,font=("time new roman",15,"bold"))
gtax_lbl.grid(row=1,column=2,padx=18,pady=15)
gtax_en=Entry(F6,bd=8,relief="groove",textvariable=tax_green_bhaji)
gtax_en.grid(row=1,column=3,ipadx=12,ipady=8)

#====================Other tax=======================
otax_lbl=Label(F6,text="OTHER TAX",bg=bg_color,fg=lbl_color,font=("time new roman",15,"bold"))
otax_lbl.grid(row=2,column=2,padx=18,pady=15)
otax_en=Entry(F6,bd=8,relief="groove",textvariable=tax_other)
otax_en.grid(row=2,column=3,ipadx=12,ipady=8)

#====================total button=====================
total_lbl=Button(F6,text="TOTAL",bg=bg_color,fg=lbl_color,font=("lucida",12,"bold"),bd=3,relief="groove",command=total)
total_lbl.grid(row=1,column=4,ipadx=30,padx=27)

#=====================genrate bill======================
gen_lbl=Button(F6,text="GENRATE BILL",bg=bg_color,fg=lbl_color,font=("lucida",12,"bold"),bd=3,relief="groove",command=bill_area)
gen_lbl.grid(row=1,column=5,ipadx=30,padx=27)

#===========================clear========================
clear_lbl=Button(F6,text="CLEAR",bg=bg_color,fg=lbl_color,font=("lucida",12,"bold"),bd=3,relief="groove",command=clear)
clear_lbl.grid(row=1,column=6,ipadx=20,padx=27)

#===========================exit========================
exit_lbl=Button(F6,text="EXIT",bg=bg_color,fg=lbl_color,font=("lucida",12,"bold"),bd=3,relief="groove",command=exit)
exit_lbl.grid(row=1,column=7,ipadx=20,padx=27)




root.mainloop()
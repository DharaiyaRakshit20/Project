import datetime
str1="Wellcome To Mallhar Dhosa"
print(str1.center(50))
name=input("Enter Your Name :")
bill_num=int(input("Enter bill number : "))
item='''
    No.\t\tDosa Item\t\tPrice\n
    1.\t\tMasala Dhosa\t\t80.00\n
    2.\t\tPalak paneer Dhosa\t150.00\n
    3.\t\tChizze Dhosa\t\t145.00\n
    4.\t\tJini Roll\t\t160.00\n
    5.\t\tMaysur Dhosa\t\t190.00\n
    6.\t\tExit
'''
data={}
while True:
    print(item)
    net_amount=0

    s_item=int(input("Enter A Select Item Number : "))
    if s_item == 1:
        print("Thank You For Your Order\n You Have Selected Masala Dhosa.")
        q1=int(input("Enter A Quntity : "))
        amount1= q1 * 80.00
        print(f"\nAmount is {amount1}")
        net_amount+=amount1
        if "item1" in data.keys():
            data["item1"]["quntity"]+=q1
            data["item1"]["amount"]+=amount1
        else:
            data.update({"item1":{"quntity":q1,"amount":amount1}})
    elif s_item == 2:
        print("Thank You For Your Order\n You Have Selected Palak paneer Dhosa.")
        q2=int(input("Enter A Quntity : "))
        amount2= q2 * 150.00
        print(f"\nAmount is {amount2}")
        net_amount+=amount2
        if "item2" in data.keys():
            data["item2"]["quntity"]+=q2
            data["item2"]["amount"]+=amount2
        else:
            data.update({"item2":{"quntity":q2,"amount":amount2}})
    elif s_item == 3:
        print("Thank You For Your Order\n You Have Selected Chizze Dhosa.")
        q3=int(input("Enter A Quntity : "))
        amount3= q3 * 145.00
        print(f"\nAmount is {amount3}")
        net_amount+=amount3
        if "item3" in data.keys():
            data["item3"]["quntity"]+=q3
            data["item3"]["amount"]+=amount3
        else:
            data.update({"item3":{"quntity":q3,"amount":amount3}})
    elif s_item == 4:
        print("Thank You For Your Order\n You Have Selected Jini Roll.")
        q4=int(input("Enter A Quntity : "))
        amount4= q4 * 80.00
        print(f"\nAmount is {amount4}")
        net_amount+=amount4
        if "item4" in data.keys():
            data["item4"]["quntity"]+=q4
            data["item4"]["amount"]+=amount4
        else:
            data.update({"item4":{"quntity":q4,"amount":amount4}})
    elif s_item == 5:
        print("Thank You For Your Order\n You Have Selected Maysur Dhosa.")
        q5=int(input("Enter A Quntity : "))
        amount5= q5 * 80.00
        print(f"\nAmount is {amount5}")
        net_amount+=amount5
        if "item5" in data.keys():
            data["item5"]["quntity"]+=q5
            data["item5"]["amount"]+=amount5
        else:
            data.update({"item5":{"quntity":q5,"amount":amount5}})
    elif s_item == 6:
        print("Thank You For Visit.")
        break
print(data)
file=open("Bill.txt","a")
keys_all=data.keys()
final_amount=0
for i in keys_all:
    main_data=data[i]
    final_amount+=main_data["amount"]
print(file.write("\n\nWellcome To malhar Dosa\n"))
x=datetime.datetime.now()
print(file.write(x.strftime("%Y/%B/%d,%H:%M:%S\n")))
print(file.write (f"Customer Name : {name}\n"))
print(file.write(f"Bill No. : {bill_num}\n"))
print(file.write("--------------------------------------------------------\n"))

print(file.write("item\t\t\tqun\t\t\tamount\n"))

print(file.write("--------------------------------------------------------\n"))
for i in keys_all:
    main_data=data[i]
    q=data[i]["quntity"]
    a=data[i]["amount"]
    print(file.write(f"{i}\t\t\t{q}\t\t\t{a}\n"))
print(file.write("--------------------------------------------------------\n"))
print(file.write("--------------------------------------------------------\n"))
print(file.write(f"Total  amount : {final_amount}\n"))

file.close()
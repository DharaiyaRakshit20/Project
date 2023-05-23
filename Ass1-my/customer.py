from manger import *
def customer_reole():  # function defination
    while True : #user while loop
        print(store)
        dict1={}
        user_choice=input("select Your Fruit : ")
        if user_choice in store.keys():  #user_choice in store.keys for if statment
            F_qty=int(input("Enter Fruit Quntity : "))
            store[user_choice]["quantity"]-=F_qty  #- to user fruit Qty
            dict1={user_choice:{"quantity":F_qty,"Amount":F_qty * store[user_choice]["Price"]}}
            print(dict1)
            print("Avelable Fruits : ",store[user_choice])
        else:
            print("Fruit not exiesting your stock")
        yn=input("Press Y for yes and N for no : ")
        if yn == 'y':
            continue
        elif yn == 'n':
            break
                     

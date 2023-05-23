store={}
F_price=0
def bill():
    pass
def Add_Fruit_Stock():  # function defination
    print("ADD FRUIT STOCK")
    F_name=input("Enter Fruit Name : ")  #user fruit name
    F_que=int(input("Enter Qty (in kg) : "))  #user fruit Qty for kg
    F_price=int(input("Enter Price (in kg): "))  #user input fruit price for per kg
    print(f"Fruit Name : {F_name}\nFruit Qty : {F_que}\nFruit Price : {F_price}")
    global store #global variable
    store.update({F_name:{"quantity":F_que,"Price":F_price}})   #update for store variable
def View_Fruit_Stock():  # function defination
    print("View Fruit Stock")
    print(store)
def Update_Fruit_Stock():   # function defination
    print("Update Fruit Stock")
    S_Fruit=input("Enter Fruit Name :")
    if S_Fruit in store.keys():  #S_fruit in store.key for if statment
        F_qty=int(input("Enter Fruit Quntity : "))
        store[S_Fruit]["quantity"]+=F_qty  #manager update Qty 
    else:
        print("Fruit not exiesting your stock")
           
    
def Customer():    # function defination
    print("Fruit Market Customer")

   
    

from manger import *    # import manger (*) mines  oll function import
from customer import *   # import customer (*) mines  oll function import 



while True:
    print("Wellcome To Fruit Market")
    item='''\n      
    1) Manger
    2) Customer
    3) Go To Exit
    '''               # user choice
    print(item)   # display  role
    s_role=int(input("Enter Your Role : ")) #input role
    if s_role == 1:   #user select 1 role to manger
        print("Fruit Market manger")      
        choice='''
        1)Add Fruit Stock
        2)View Fruit Stock
        3)Update Fruit Stock   
        '''
        while True:
                print(choice)   #display choice
                s_choice=int(input("Select Your Choice : "))
                if s_choice == 1:  #user select 1 choice to Add fruit stock
                    Add_Fruit_Stock()  # function call
                    yn=input("Press Y for yes and N for no : ")
                    if yn == 'y':  #user 'y' for yes to continue to program
                        continue
                    elif yn == 'n':  #uesr 'n' for no to break to program
                        break
                elif s_choice == 2:  #user select 2 choice to View fruit stock
                    View_Fruit_Stock()  #function call
                    yn=input("Press Y for yes and N for no : ")
                    if yn == 'y': #user 'y' for yes to continue to program
                        continue
                    elif yn == 'n': #user 'n' for no to break to program
                        break  
                elif s_choice == 3:
                    Update_Fruit_Stock()  # function call
                    yn=input("Press Y for yes and N for no : ")
                    if yn == 'y':  #user 'y' for yes to continue to program
                        continue
                    elif yn == 'n':  #user 'n' for no to break to program
                        break
    elif s_role == 2:  #user select 2 role to customer
        customer_reole()  # function call
        
    elif s_role == 3:  #user select 3 role to Got back to program
        print(store)
        total_amount=0
        file=open("FMC.txt","a")
        print(file.write("\n\nFruit Market Customer\n"))
        name=input("Enter Customer Name : ")
        print(file.write(f"Name : {name}\n"))
        Bill_num=int(input("Enter Bill Number : "))
        print(file.write(f"Bill No. : {Bill_num}\n"))
        print(file.write("------------------------------------\n"))
        print(file.write("------------------------------------\n"))
        print(file.write("item\t\tQty\t\tprice\n"))
        print(file.write("------------------------------------\n"))
        for i in store:
            qty=store[i]["quantity"]
            pr=store[i]["Price"]
            print(file.write(f"{i}\t\t{qty}\t\t{pr}\n"))
            total_amount+=pr
        print(file.write("------------------------------------\n"))
        print(file.write(f"Total Amount\t\t\t{total_amount}\n"))
        print(file.write("------------------------------------\n"))
        break
        

        
        
        
            
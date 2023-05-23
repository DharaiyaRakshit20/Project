from Counsellor import *
def Add_mark_student():
    while True:
        user_choice=int(input("select Your Serial Number : "))
        if user_choice in store.keys():
            U_Subject=input("Enter Subject :")
            if U_Subject in store[user_choice]["Subject"]:
                u_marks=int(input("Enter A Add Marks :"))
                position=store[user_choice]["Subject"].index(U_Subject)
                store[user_choice]["Marks"][position]+=u_marks
                print(f"Add Marks : {store}")
        
        else:
            print("Student not exiesting your list")

def View_All_Student():
    print(store)
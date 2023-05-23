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
    for student in store:
        print(f"All Student Serial Number : {student}")
        print("First Name--------------")
        print(store[student]["First_Name"])
        print("Last Name--------------")
        print(store[student]["Last_Name"])
        print("Contact Number--------------")
        print(store[student]["Countect_Number"])
        print("Subject--------------")
        print(store[student]["Subject"])
        print("Marks--------------")
        print(store[student]["Marks"])
        print("Fees--------------")
        print(store[student]["Fees"])
        print("----------------------------------\n")
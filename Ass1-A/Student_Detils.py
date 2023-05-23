from Counsellor import *
def student_detials():
    student=int(input("Enter Serial Number : "))
    if student in store.keys():
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
    else:
        print("Not A Student Serial Number")
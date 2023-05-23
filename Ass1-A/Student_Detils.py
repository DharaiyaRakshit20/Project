from Counsellor import *
def student_detials():
    student=int(input("Enter Serial Number : "))
    if student in store.keys():
        print(store[student]["First_Name"])
        print(store[student]["Last_Name"])
        print(store[student]["Countect_Number"])
        print(store[student]["Subject"])
        print(store[student]["Marks"])
        print(store[student]["Fees"])
    else:
        print("Not A Student Serial Number")
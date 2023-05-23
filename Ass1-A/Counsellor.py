store={}
def Add_Student():
    print("Add Student")
    A_number=int(input("Enter A Serial Number : "))
    A_Fname=input("Enter A First Name : ")
    A_Lname=input("Enter A Last Name : ")
    A_Cnumber=int(input("Enter A Contect Number : "))
    subjectlist=[]
    marklist=[]
    feeslist=[]
    for i in range(1,3):
        A_subject=input(f"Enter A Subject {i}: ")
        subjectlist.append(A_subject)
        A_mark=int(input(f"Enter A marks {i}: "))
        marklist.append(A_mark)
        A_fees=int(input(f"Enter A Fees {i}: "))
        feeslist.append(A_fees)
        print("--------------------------")

    global store
    store.update({A_number:{"First_Name":A_Fname,"Last_Name":A_Lname,"Countect_Number":A_Cnumber,"Subject":subjectlist,"Marks":marklist,"Fees":feeslist}})


def Remove_Student():
    print("Remove Student ")
    serial_number=int(input("Enter Remove Serial Number : "))
    if serial_number in store.keys():
        store.pop(serial_number)
        
    else:
        print("Student not exiesting your Student List.")

def view_all_student():
    print("View All Student")
    # print(store)y
    for student in store.keys():
        print(f"Student Serial Number : {student}")
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
        print("-----------------------------\n")

def Specific_Student():
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
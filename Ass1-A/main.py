from Counsellor import *
from Faculty import *
from Student_Detils import *
while True:
    item='''
    1) Press 1 For Counsellor
    2) press 2 For Faculty
    3) Press 3 For Student
    4) Press 4 For Go To Exit
    '''
    print(item)
    role=int(input("Enter A Role ID : "))
    if role == 1:
        print("WellCome To Counsellor")
        C_item='''
        1.Add Student
        2.Remove Student
        3.View All Student
        4.view Specific Student 
        '''
        while True:
            print(C_item)
            C_choice=int(input("Enter A Choice by Counsellor : "))
            if C_choice == 1:
                Add_Student()
                yn=input("Press Y for yes and N for no : ")
                if yn == 'y':  #user 'y' for yes to continue to program
                    continue
                elif yn == 'n':  #uesr 'n' for no to break to program
                    break
            elif C_choice == 2:
                Remove_Student()
                yn=input("Press Y for yes and N for no : ")
                if yn == 'y':  #user 'y' for yes to continue to program
                    continue
                elif yn == 'n':  #uesr 'n' for no to break to program
                    break
            elif C_choice == 3:
                view_all_student()
                yn=input("Press Y for yes and N for no : ")
                if yn == 'y':  #user 'y' for yes to continue to program
                    continue
                elif yn == 'n':  #uesr 'n' for no to break to program
                    break
            elif C_choice == 4:
                Specific_Student()
                yn=input("Press Y for yes and N for no : ")
                if yn == 'y':  #user 'y' for yes to continue to program
                    continue
                elif yn == 'n':  #uesr 'n' for no to break to program
                    break
    elif role == 2:
        print("Wellcome To Faculty")
        F_item='''
        1.Add Mark To Student
        2.View All Student
        '''
        while True:
            print(F_item)
            F_Choice=int(input("Enter A Choice by Faculty : "))
            if F_Choice == 1:
                Add_mark_student()
                yn=input("Press Y for yes and N for no : ")
                if yn == 'y':
                    continue
                elif yn == 'n':
                    break
            elif F_Choice == 2:
                View_All_Student()
                yn=input("Press Y for yes and N for no : ")
                if yn == 'y':
                    continue
                elif yn == 'n':
                    break
    elif role == 3:
        print("Wellcome To Student")
        student_detials()
    elif role == 4:
        print("Thank You For Visit.")
        break
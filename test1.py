all=list()

def add():
       student=list()
       student.append(input("enter your first name: "))
       student.append(input("enter you last name: "))
       student.append(input("enter your id number: "))
       all.append(student)
      

def show():
    for student in all:
           print(*student,sep=",")

def edit():
    edit_id=input("enter your selected id: ")

    for student in all:
        if student[2]==edit_id:
            student[0]=input("enter your first name: ")
            student[1]=input("enter your last name: ")
            break
    else:
       print("invalid id")

def delet():
    delet_id=input("enter your selected id: ") 

    for student in all:
        if student[2]==delet_id:
         all.remove(student)
         break
          
    
while True:
 print("1.add student \n 2.show student \n 3.edit student \n 4.delet student \n 5.exit")
 number=int(input("enter your number: "))

 if number==1:
     add()
 elif number==2:
    show()
 elif number==3:
     edit()
 elif number==4:
     delet()
 elif number==5:
     break  
 else:
    print("invalid input.")
     




    





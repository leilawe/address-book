all=list()

while True:
 number=int(input("enter your number: "))

 if number==1:
       student=list()
       student.append(input("enter your first name: "))
       student.append(input("enter you last name: "))
       student.append(input("enter your id number: "))
       all.append(student)
    
    
 elif number==2:
     for student in all:
           print(*student,sep=",")

 elif number==3:
    edit_id=input("enter your selected id: ")
    for student in all:
        if student[2]==edit_id:
            student[0]=input("enter your first name: ")
            student[1]=input("enter your last name: ")
            break
    else:
        print("invalid id")

 elif number==4:
    delet_id=input("enter your selected id: ") 
    for student in all:
        if student[2]==delet_id:
         all.remove(student)
         break
    else:
        print("invalid id")
 elif number==5:
     break

 else:
    print("invalid input.")


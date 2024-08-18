
# print("1.add student \n 2.show student \n 3.edit student \n 4.delet student \n 5.show the best score")
# # number=int(input("enter ur number: "))
all_student=list()

while True:
 
 print("1.add student \n 2.show student \n 3.edit student \n 4.delet student \n 5.show the best score")
 number=int(input("enter ur number: "))


 if number==1:

  student_dict={

    "name": input(" enter ur first and last name: "),
    "birthday" : input(" enter your date of birth: "),
    "id_number" : input("enter your id number: "),
    "gender" : input("what is your gender? "),
    "math_score" :float(input("enter your math score: ")),
    "english_score" :float(input("enter your english score:")),
    "literature_score" :float(input("enter your literature score: ")),
   }
  student_dict["average"]=(student_dict["english_score"] +student_dict["literature_score"]+ student_dict["math_score"]) / 3
  all_student.append(student_dict)

 
 elif number==2:
   print(*all_student)
 
 
 elif number==3:
    edit_id=input("enter your selected id: ")
    for index in range (len(all_student)):
        if all_student[index]["id_number"]==edit_id:
            student_dict["name"]=input("enter your first and last name: ")
            student_dict["birthday"]=input("enter your date of birth: ")
            student_dict["gender"]=input("enter your gender: ")
            student_dict["math_score"]=input("enter your math score: ")
            student_dict["english_score"]=input("enter your english score: ")
            student_dict["literature_score"]=input("enter your literature score: ")
            student_dict["average"]=(student_dict["english_score"] +student_dict["literature_score"]+ student_dict["math_score"]) / 3
            break
    else:
      print("there is no student with this id! ")  


 elif number==4: 
   deleted_id=input("enter your selected id: ")
   for index in range (len(all_student)):
    if all_student[index]["id_number"]==deleted_id:
      del all_student[index]
      break
     
   else:
     print("invalid id! ")
  
 elif number==5: 
    max=0  
    for index in range(len(all_student)):
      if max< all_student[index]["average"]:
        max=all_student[index]["average"]
        name=all_student[index]["name"]
        
    print(name, max)    
   
 






#  for id_number in student_dict:
#   if student_dict["id_number"]==id_number:
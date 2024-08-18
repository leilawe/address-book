allproducts=list()

def checkid_number():
 product_id=input("enter the product id you want to edit: ")
 for index in range(len(allproducts)):
  if allproducts[index]["product_id"]==product_id:
   return index
  else:
   continue
 else:
  print("invalid id! ") 


while True:
   print(" 1) admin menu \n 2) user menu ")
   number=int(input("which option do you choose? "))

 
   while True:
    if number==1:
     users=[
   { "user": "admin",
    "password": "1234"
   }
   ]
    user=input("enter your user name: ")
    password=input("enter your password:")
    for i in range(len(users)):
     if user==users[i]["user"] and password==users[i]["password"]:
      while True:
       print(f"welcome {user}")

       print(" 1) add a product \n 2) show all products \n 3) edit product \n 4) favorite product  \n 5) show inventory \n 6) main menu ") 
       ch=int(input("which item do you choose? "))
    
       if ch==1:
        products_dict={
        "productname":input("enter your product name: "),
        "productid": int(input("enter your product id: ")),
        "productinventory":int(input("enter your product inventory: ")),
        "productprice":float(input("enter your product price: ")),
        "favorite":"0"
        }
        allproducts.append(products_dict)
        print("product added successfully")
    
  
       elif ch==2:
        print(allproducts)

       elif ch==3: 
        print(" 1) product name \n 2) product id \n 3) product inventory \n 4) product price ")
        ch2=int(input("which item do you choose? "))
        if ch2==1:
         edited_name= checkid_number()
         allproducts[edited_name]["name"]=input("enter your new product name: ")
        elif ch2==2:
         edited_id= checkid_number()
         allproducts[edited_id]["id"]=input("enter your new product id: ")
        elif ch2==3:
         edited_inventory=checkid_number()
         allproducts[edited_inventory]["inventory"]=input("enter your new product inventory")
        elif ch2==4:
         edited_price=checkid_number()
         allproducts[edited_price]["price"]=input("enter your new product price: ")
        
        elif ch==4:
         best_selling=0
         for i in range(len(allproducts)):
          if best_selling< [i]["favorite"]:
           best_selling=allproducts[i]["favorite"]
           favorite=allproducts[i]["favorite"]

          print("name", favorite ) 

       elif ch==5:
        print("name", "inventory")
        






           




       
       
   
 

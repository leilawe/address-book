import csv

contacts=[]

def view_contacts():
   print("your Address Book: ")     
   for contact in contacts:
      print(f"name: {contact['name']}") 
      print(f"phone: {contact['phone']}") 
      print(f"email: {contact['email']}") 
      print(f"address: {contact['address']}") 
      print("-" *30)


def add_contact():
   with open("address_book.csv", "w"):
    print("add a new contact ")
    name= input("name: ")
    phone= input("phone: ")  
    email= input("email: ")
    address= input("address: ")


    if not phone.isdigit():
      raise ValueError("phone number must be numeric! ")
   
    contact= {"name": name, "phone": phone, "email": email, "address": address}
    contacts.append(contact)
    save_contacts()
    print(f"{name} has been added to your address book.")
 
def save_contacts():
   try:
     with open("address_book.csv","w",newline=""):
       headar_names=["name","phone","email","address"]
       writer=csv.DictWriter(__file__, fieldnames=headar_names)
       writer.writeheader()
       writer.writerows(contacts)
   except Exception as e:
      print("not connected!")
def open_file():
    try:
      with open("address_book.csv", "r")as file:
        lines= csv.DictReader(file)
        for line in lines:
            contacts.append(line)
    except FileNotFoundError:
       print("this file does not exist.")


def update_contact():
   print("update a contact")   
   phone= input("enter the phone number of the contact to update: ") 
   if not phone.isdigit():
      raise ValueError("phone number must be numeric! ") 
   for contact in contacts:
      if contact["phone"]==phone:
       print(f"current details for {contact["name"]}:") 
       print(f"name: {contact['name']}") 
       print(f"phone: {contact['phone']}") 
       print(f"email: {contact['email']}") 
       print(f"address: {contact['address']}") 
       print("-" *30)


      new_name = input("new name (press enter if you want to keep current): ").strip()
      new_email = input("new email (press enter if you want to keep current): ").strip()
      new_address = input("new address (press enter if you want to keep current): ").strip()

      if new_name:
         contact["name"]= new_name
      elif new_email:
         contact["email"]= new_email
      elif new_address:
         contact["address"]= new_address

      save_contacts()    
      print(f"contact details for {contact["name"]} haave been updated.")  
      return

   print("contact not found. ")



def delete_contact():
   print("delet a contact")   
   phone= input("enter the phone number of the contact to delet: ") 
   if not phone.isdigit():
      raise ValueError("phone number must be numeric! ")   

   for contact in contacts:
      if contact["phone"]==phone:
         deleted_name=contact["name"]
         contacts.remove(contact) 
         save_contacts()  
         print(f"contact {deleted_name} has been deleted from your address book. ")
         return

   print("contact not found. ")
   
open_file()
while True:
    try:
       print()
       print("Address book menu: " )     
       print("1) Add contact") 
       print("2) view contacts") 
       print("3) update contact")
       print("4) delete contact")
       print("5) exit")

       choice=int(input("enter your choice (1/2/3/4/5): ").strip())

       if choice==1:
          add_contact()
       elif choice==2:
          view_contacts()
       elif choice==3:
          update_contact()
       elif choice==4:
          delete_contact()   
       elif choice==5:
          print("goodbye")
          exit()       
       else:
         print("invalid choice, please try again! ") 
    except Exception as e:
       print(f"Error: {e}")


           
      


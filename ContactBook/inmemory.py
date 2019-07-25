from beautifultable import BeautifulTable
from Contact_new import Contact


class InMemoryImpl:

    contact_list = []  

    @classmethod
    def addContact(cls):
        name = input("enter name: ")
        email = input("enter email: ")
        mobile = input("enter mobile: ")
        address = input("enter address: ")
        cls.contact_list.append(Contact(name, email, mobile, address))
        print(f"Contact is added succesfully!!! with name: {name} ")

    @classmethod
    def deleteContact(cls):
        name = input("enetr name to delete: ")
        contact = cls.get_contact_by_name(name)
        if contact:
            cls.contact_list.remove(contact)
            print(f"contact: {name} deleted successfully!!!!")
        else:
            print(f"contact with name : {name} not found")

        
    @classmethod
    def viewContact(cls):
        InMemoryImpl._paint(cls.contact_list)
    
    @classmethod
    def search(cls):
        if len(cls.contact_list) > 0 :
            name = input("enetr name to search: ")
            s_list = list(filter(lambda x:name.lower() in x.get_name().lower(),cls.contact_list))
            if len(s_list) > 0:
                InMemoryImpl._paint(s_list)
            else:
                print("there is no data found with searched name: {name}")
        else:
            print("Contact book is empty!!..... You cant search!!!")

    
    @classmethod
    def get_contact_by_name(cls, name):

        if len(cls.contact_list) > 0:
            contact = list(filter(lambda x:x.get_name().lower() == name.lower(), cls.contact_list))
        return contact[0] if contact else None


    
    @classmethod
    def updateContact(cls):
        name = input("enetr name to update: ")
        contact = cls.get_contact_by_name(name)
        if contact:
            print("1.Name 2.Email 3.Mobile 4.Address")
            ch = int(input("enter your choice: "))
            if ch == 1:
                print(f"Old name: {contact.get_name()}")
                name= input("entyer the new name: ")
                if name:
                    contact.set_name(name)
            
            elif ch == 2:
                print(f"Old email: {contact.get_email()}")
                email= input("entyer the new email: ")
                if email:
                    contact.set_email(email)
            
            elif ch == 3:
                print(f"Old mobile: {contact.get_mobile()}")
                mobile= input("entyer the new mobile: ")
                if mobile:
                    contact.set_mobile(mobile)

            elif ch == 4:
                print(f"Old address: {contact.get_address()}")
                address= input("entyer the new address: ")
                if address:
                    contact.set_address(address)
        else:
            print(f"contact not found with name: {name}")

    @staticmethod
    def _paint(lst):
        if len(lst) != 0:
            table=BeautifulTable()
            table.column_headers = ["Name", "Email", "Mobile", "Address"] 
            for c in lst:
                table.append_row([c.get_name(),c.get_email(), c.get_mobile(), c.get_address()])
            print(table)
        else:
            print(f"Contact Book is empty!.....")
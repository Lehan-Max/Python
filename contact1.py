from contact import Contact

class ContactBook:

    contacts = []

    @staticmethod
    def addContact():
        name = input("enter the name: ")
        email = input("enter the email: ")
        mobile = input("enter the mobile: ")
        ContactBook.contacts.append(Contact(name,email,mobile))

    @staticmethod
    def searchContact():
        name = input("enter name to search:  ")
        
        #logic
        

    @staticmethod
    def deleteContact():
        name = input("enter name to delete")
        #logic

    @staticmethod
    def viewAll():
        pass

    @staticmethod
    def update():
        
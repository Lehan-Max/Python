class Contact:

    def __init__(self, name, email, mobile, address):
        self.name = name
        self.email = email
        self.mobile = mobile
        self.address = address
        
    def get_name(self):
 	    return self.name
 
    def set_name(self, name) :
 	    self.name = name

    def get_email(self):
        return self.email
                            
    def set_email(self, email) :
        self.email = email

    def get_mobile(self):
        return self.mobile
                            
    def set_mobile(self, mobile) :
        self.mobile = mobile

    def get_address(self):
        return self.address
                            
    def set_address(self, address) :
        self.address = address

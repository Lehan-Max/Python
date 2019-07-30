class MaxLimitError(Exception):

    def __init__(self,message):
        self.message = message
    
    def __str__(self):
        return f"{self.__class__.__name__}:{self.message}"

c = 0
def login(username, password):
    global c
    if username == "abc" and password == "cba":
        print("login successful ")
        print("hello Buddy!!!!!")
    else:
        print("Bad credentials.....")
        c += 1
    if c > 2:
        raise MaxLimitError("You have reached maximum number of attempts...")        
login("ABC","CBA")
login("d","f")
login("a","c")
login("abc","cba")
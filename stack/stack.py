class Stack:
    
    def __init__(self):
        self.st=[]
    
    def push(self):
        num = int(input("enter numer to stack: "))
        self.st.append(num)
        print("Push success")
        

    def pop(self):
        if self.is_empty():
            print("underflow")
        else:
            ele = self.st.pop()
            print(f"{ele} : just popped")
    
    def display(self):
        if self.is_empty():
            print("stack is empty")
        else:
            print("elements in the stack are: ")
            for i in range(len(self.st)-1,-1,-1):
                print(self.st[i])


    def search(self):
        if self.is_empty():
            print("underflow")
        else:
            num = int(input("enter the ele to search: "))
            if num in self.st:
                print(f"element found at pos {self.st.index(num)+1}")
            else:
                print("elements not found")

    
    def is_empty(self):
        if len(self.st) == 0:
            return True
        else:
            print("elements not found")


if __name__ == "__main__":
    st = Stack()
    opt_dict={1:st.push, 2:st.pop, 3:st.display, 4:st.search, 5:exit}
    while True:
        print('*'*100)
        print('1.PUSH 2.POP 3.DISPLAY 4.SEARCH 5.EXIT')
        print('*'*100)
        try:
            ch = int(input("enter choice: "))
            ref = opt_dict[ch]
            ref()
        except (ValueError, KeyError):
            print("ENTER ONLY NUMBERS 1 TO 5")
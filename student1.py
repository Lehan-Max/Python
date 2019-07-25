class Student:
    def __init__(self, name, subjscores): #constructor
            self.name = name
            self.subscores = subjscores
    
    def average(self):
        return sum(self.subscores)/len(self.subscores)

stu_1 = Student("Lehan",[45,55,79])

print(f"{stu_1.average():.2f}")
class Student:

    def __init__(self, name): #constructor
            self.name = name
            self.subscores = []
    
    def average(self):
        return sum(self.subscores)/len(self.subscores)

stu_1 = Student("Lehan")
stu_1.subscores.extend([45,55,79])
print(f"{stu_1.average():.2f}")



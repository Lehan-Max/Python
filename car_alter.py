class Car:

    def __init__(self,model, regno, no_gears):
        self.model = model
        self.regno = regno
        self.no_gears = no_gears
        self.is_started = False
        self.c_gear = 0

    def start(self):
        if self.is_started:
            print(f"{self.model} with reg_no: {self.regno} is already started")
        else:
            print(f"{self.model} with reg_no: {self.regno} started....")
            self.is_started = True
    
    def stop(self):
        if self.is_started:
            print(f"{self.model} with reg_no: {self.regno} stopped....")
            self.is_started = False
        else:
            print(f"{self.model} with reg_no: {self.regno} has already stopped....")
            

    def change_gear(self):
        if self.is_started:
            if self.c_gear < self.no_gears:
                self.c_gear += 1
                print(f"{self.model} with reg_no: {self.regno} changed gear....")
            else:
                print(f"{self.model} with reg_no: {self.regno} already on top gear....")
        else:        
            print(f"{self.model} with reg_no: {self.regno} has already stopped... can't change gear....")

    def showInfo(self):
        print(f"Name: {self.model} - regno: {self.regno} - Started: {self.is_started} - No of gears: {self.no_gears} - gear_count: {self.c_gear}")
    
if __name__ == "__main__":
   
    bmw = Car("KA01300",4)
    audi = Car("KA450067",6)
    benz = Car("KA450068",5)
    Nano = Car("KA450069",4)
    

    audi.start()
    audi.stop()
    audi.change_gear()

lst = [bmw, audi, benz, Nano]
for car in lst:
    car.showInfo()
c= len(list(filter(lambda x: x.is_started and x.c_gear == 0, lst)))
print(c)    

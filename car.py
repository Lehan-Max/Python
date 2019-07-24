class Car:

    def __init__(self, regno, no_gears):
        self.regno = regno
        self.no_gears = no_gears
        self.is_started = False

    def start(self):
        if self.is_started:
            print(f"car with reg_no: {self.regno} is already started")
        else:
            print(f"car with reg_no: {self.regno} started....")
            self.is_started = True
    
    def stop(self):
        if self.is_started:
            print(f"car with reg_no: {self.regno} stopped....")
            self.is_started = False
        else:
            print(f"car with reg_no: {self.regno} has already stopped....")
            

    def change_gear(self):
        if self.is_started:
            print(f"car with reg_no: {self.regno} changed gear....")
        else:
            print(f"car with reg_no: {self.regno} has already stopped... can't change gear....")
    
if __name__ == "__main__":
    bmw = Car("KA01300",5)
    audi = Car("KA450067",6)
    bmw.start()
    bmw.change_gear()
    bmw.stop()
    bmw.stop()
    bmw.change_gear()

    audi.start()
    audi.stop()
    audi.change_gear()
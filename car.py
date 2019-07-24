class Car:

    def __init__(self, regno, no_gears):
        self.regno = regno
        self.no_gears = no_gears

    def start(self):
        print(f"{self.regno} started....")
    
    def stop(self):
        print(f"{self.regno} stopped....")
    
    def change_gear(self):
        print(f"{self.regno} changed gear....")

    
if __name__ == "__main__":
    bmw = Car("KA01300",5)
    bmw.start()
    bmw.change_gear()
    bmw.stop()
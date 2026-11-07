class Vehicle:
    def start(self):
        print("Vehicle is starting")
class Car(Vehicle):
    def drive(self):
        print("Car is being driven")
c1=Car()
c1.start()
c1.drive()
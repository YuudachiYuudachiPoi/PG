class Car():
    def __init__(self):
        self.speed = 0
        self.running = False
    def start(self):
        self.running = True
    def drive(self):
        if self.running:
            print('Car is moving')
        else:
            print('Start the car first')

class Taxi(Car):
    def __init__(self)
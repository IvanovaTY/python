class Car:
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
  
    def go(self):
        print('машина {} поехала.'.format(self.name))
    
    def stop(self):
        print('машина {} остановилась!'.format(self.name))
        
    def turn(self, direction):
        print('машина {} повернула {}.'.format(self.name, direction))
        
        
class TownCar(Car):
    def __init__(self, speed, color, name):
        Car.__init__(self, speed, color, name) 
        
class SportCar(Car):
        def __init__(self, speed, color, name):
            Car.__init__(self, speed, color, name)
        
class WorkCar(Car):
        def __init__(self, speed, color, name):
            Car.__init__(self, speed, color, name)
        
        
class PoliceCar(Car):
        def __init_(self, speed, color, name, is_police = True):
            Car.__init__(self, speed, color, name)
            self.is_police = is_police
            
car1 = Car(100,'red', 'Toyota')
    
car2 = SportCar(100, 'red', 'Toyota')
car2.turn('назад')

    

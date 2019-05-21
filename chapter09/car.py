##class test
class Car():
    """模拟汽车"""###init是两个__
    def __init__(self,make,model,year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        self.gas=0
        
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
        
    def updata_odometer(self,mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("you can not roll back an odometer")
    
    
class ElectricCar(Car):
    """电动汽车的独特之处"""
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery_size=70
    
    def describe_battery(self):
        print("This car has a "+ str(self.battery_size) + '-kWh battery')
    def fill_gas(self):
        print(self.model + " donot need gas")
        
        
my_new_car= Car('audi','a4',2016)
print(my_new_car.get_descriptive_name())
my_tesla=ElectricCar('tesla','model s',2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
my_tesla.fill_gas()

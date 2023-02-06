from car_modify_though_method import Car 
from electric_car_battery import ElectricCar

my_new_car = Car('audi','a4', 2024)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
my_electric_car = ElectricCar("nissan","leaf", 2024)
my_electric_car.battery.describe_battery()
my_electric_car.get_descriptive_name
my_electric_car.battery.get_range()
buy_car = input("sports car or luxury?")
car_type = "automatic"
gas_full = input("your gas tank is full, True or False?: ")
gas_in_tank = 0.0
gas_capacity = 12.0
mpg = 28

def car_choice():
    if buy_car == "sports":
        print ("your car is a chevy impala")
    elif buy_car == "luxury":
        print ("your car is a Lexus")

car_choice()

def car_run():
    if gas_full == "True": 
        print ("you may start the car")
    elif gas_full == "False": 
        print ("YOU NEED GAS")
    
car_run()

def drive_car(gas_in_tank):
    if gas_full == "True":
        print("Drive, you have " + str(12.0*28) + " miles left")
    elif gas_in_tank != 0.0:
        print("You can drive.  You have " + str(gas_in_tank) + " gallons left")
    elif gas_in_tank == 0.0:
        print("Fill up for "+ str(gas_capacity - gas_in_tank) + " gallons")
        
drive_car(0.0)

def fill_tank():
    if gas_full == "False":
        print("pull over now and fill up, or you'll be walking home")
    elif gas_full == "True":
        print("enjoy the ride")
        
fill_tank()

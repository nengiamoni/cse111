
import math
import datetime
# Read tire specifications from the user
width = float(input("Enter the width of the tire in mm (e.g., 205): "))
aspect_ratio = float(input("Enter the aspect ratio of the tire (e.g., 60): "))
diameter = float(input("Enter the diameter of the wheel in inches (e.g., 15): "))

#note i try using the fomula directly like this but is not giving me the right answer when am testing example given
#so i try to break the fomula down and it acqually works 
#volume = (math.pi * width ** 2 * aspect_ratio * width * aspect_ratio + 2540 * diameter) / 10000000000

#I Calculate the volume of space inside the tire
volume1 = math.pi * width ** 2 * aspect_ratio 
volume2=width*aspect_ratio+2540*diameter
volume3=volume1*volume2
volume4=volume3/10000000000

# I Display the calculated volume
print(f"The approximate volume is {volume4:.2f} liters")

current_date = datetime.datetime.now().strftime("%Y-%m-%d")

# Open the 'volumes.txt' file for appending and add the data
with open('volumes.txt', 'a') as file:
    file.write(f"{current_date}, {width}, {aspect_ratio}, {diameter}, {volume4:.2f}\n")

#i exceed the core requiremnts 

#I layout the tire specofication and their price respectively 
tire_prices = {
    (185, 50, 14): 99.99,
    (205, 60, 15): 119.99,
    (305, 70, 16): 138.99,
}

tire_specification= (width, aspect_ratio, diameter)
if tire_specification in tire_prices:
    price = tire_prices[tire_specification]
    print(f"The price for these tires is ${price:.2f}")
else:
    print("Tire prices for these specifications are not available in our database")

buy_tires = input("Do you want to buy these tires? (yes/no): ").lower()

if buy_tires == "yes":
        # I Collect the user's phone number
        phone_number = input("Please enter your phone number: ")
        # i Get the current date
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        
        with open('volumes.txt', 'a') as file:
            file.write(f"{current_date}, {width}, {aspect_ratio}, {diameter}, {volume4:.2f}, {phone_number}\n")
        print("Thank you for your purchase! Your order has been recorded.")
   
else:
   print("Tire prices for these specifications are not available in our database.")
   print("Thank you for using our tire volume calculator.")
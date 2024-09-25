# Exercise 2: Ohm's Law Calculator
# Creating Functions for each Formula
def voltage_formula(current, resistance):
    return current * resistance

def current_formula(voltage, resistance):
    if resistance == 0:
        raise ZeroDivisionError("Sorry, Resistance cannot be Zero.")
    return voltage / resistance

def resistance_formula(voltage, current):
    if current == 0:
        raise ZeroDivisionError("Sorry, Current cannot be Zero.")
    return voltage / current

# Creating the Calculator
while True:
     # Creating The User Prompt
    try:
        print("What Do You Want to Calculate?")
        print("Press 'V' for Voltage, 'I' for Current, 'R' for Resistance")
        choice = str(input("Enter Your Choice ('V', 'I', or 'R'): ")).upper()
        
        # Calculator for Voltage 
        if choice == "V":
            current = float(input("Enter the Current (in Amps): "))
            resistance = float(input("Enter the Resistance (in Ohms): "))
            voltage = voltage_formula(current, resistance)
            print(f"The Voltage is {round(voltage, 2)} V")
        # Calculator for Current 
        elif choice == "I":
            voltage = float(input("Enter the Voltage (in Volts): "))
            resistance = float(input("Enter the Resistance (in Ohms): "))
            current = current_formula(voltage, resistance)
            print(f"The Current is {round(current, 2)} A") 
        # Calculator for Resistance
        elif choice == "R":
            voltage = float(input("Enter the Voltage (in Volts): "))
            current = float(input("Enter the Current (in Amps): "))
            resistance = resistance_formula(voltage, current)
            print(f"The Resistance is {round(resistance, 2)} Ω")   
        # Other Possible Options
        else:
            print("Please Enter Valid Options ('V', 'I', or 'R').")
            continue
        break
    # Handle the Exceptions
    except ValueError:  
        print("You have put an Invalid Input, Please Enter Numeric Value for voltage, current, and resistance.")

    except ZeroDivisionError as error_message:
        print(error_message)
 
import math
from datetime import date

width = float(input("Enter the width of the tire in mm (ex 205): "))

aspect_ratio = float(input("Enter the aspect ratio of the tire (ex 60): "))

diameter = float(input("Enter the diameter of the wheel in inches (ex 15): "))

volume = (math.pi * (width ** 2) * aspect_ratio * (width * aspect_ratio + 2540 * diameter)) / 10000000000

print(f"\nThe approximate volume is {volume:.2f} liters")

# Get current date (no time)
today = date.today()

with open("volumes.txt", "a") as file:
    file.write(f"{today}, {width}, {aspect_ratio}, {diameter}, {volume:.2f}\n")

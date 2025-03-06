import math

width = int(input("Please enter the width of the tire in millimeters: "))
aspect_ratio = int(input("Please enter the aspect ratio of the tire: "))
diameter = int(input("Please enter the diameter of the wheel in inches: "))

volume = (math.pi * (width)**2 * aspect_ratio * (width * aspect_ratio + 2540 * diameter)) / 10000000000

print(f"The volume inside your tire is {volume:.2f} liters.")
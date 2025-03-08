import math
from datetime import datetime

width = int(input("Please enter the width of the tire in millimeters: "))
aspect_ratio = int(input("Please enter the aspect ratio of the tire: "))
diameter = int(input("Please enter the diameter of the wheel in inches: "))

volume = (math.pi * (width)**2 * aspect_ratio * (width * aspect_ratio + 2540 * diameter)) / 10000000000

print(f"The volume inside your tire is {volume:.2f} liters.")


# exceeding requirements
if width == 205 and aspect_ratio == 55 and diameter == 16:
  print("This tire size is commonly found on midsize sedans and has the approximate cost range of $66 - $253 per tire.")
elif width == 215 and aspect_ratio == 60 and diameter == 16:
  print("This tire size is commonly found on small SUVs and has the approximate cost range of $75 - $200 per tire.")
elif width == 225 and aspect_ratio == 65 and diameter == 17:
  print("This tire size is commonly found on  SUVs and has the approximate cost range of $100 - $250 per tire.")
elif width == 265 and aspect_ratio == 70 and diameter == 17:
  print("This tire size is commonly found on light trucks and larger SUVs and has the approximate cost range of around $200 per tire.")

current_datetime = datetime.now(tz=None)

with open("volumes.txt", mode="at") as volumes_file:
  print(f"{current_datetime:%Y-%m-%d}, {width}, {aspect_ratio}, {diameter}, {volume:.2f}", file=volumes_file)

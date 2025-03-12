# # Example 3
# import math
# def main():
#   radius = float(input("Enter the radius of a circle: "))
#   area = circle_area()
#   print(f"area: {area:.1f}")
# def circle_area():
#   # Mistake! There is no variable named radius
#   # defined inside this function, so the variable
#   # radius cannot be used in this function.
#   area = math.pi * radius * radius
#   return area
# main()

# # Example 4
# import math
# def main():
#   radius = float(input("Enter the radius of a circle: "))
#   area = circle_area(radius)
# print(f"area: {area:.1f}")
#   def circle_area(radius):
#   area = math.pi * radius * radius
#   return area
# main()

import math

def circle_area(radius):  # Define this function outside of main
    area = math.pi * radius * radius
    return area

def main():
    radius = float(input("Enter the radius of a circle: "))
    area = circle_area(radius)  # Call the function correctly
    print(f"area: {area:.1f}")  # Correct indentation

main()

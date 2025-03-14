import math

radius = [6.83, 7.78, 8.73, 10.32, 10.79, 13.02, 5.40, 6.83, 15.72, 6.83, 7.62, 8.10]

height = [10.16, 11.91, 11.59, 11.91, 17.78, 14.29, 8.89, 7.62, 17.78, 12.38, 11.27, 11.11]

can_name = ["#1 Picnic", "#1 Tall", "#2", "#2.5", "#3 Cylinder", "#5", "#6Z", "#8Z short", "#10", "#211", "#300", "#303"]

def main():
  # Stretch Challenge 3
  for i in range(len(radius)):
    volume = compute_volume(radius[i], height[i])
    surface_area = compute_surface_area(radius[i], height[i])
    storage_efficiency = volume / surface_area
    cans = can_name[i]

    print(f"{cans} {storage_efficiency:.2f}")

def compute_volume(radius, height):
  return math.pi * radius ** 2 * height

def compute_surface_area(radius, height):
  return 2 * math.pi * radius *(radius + height)

main()
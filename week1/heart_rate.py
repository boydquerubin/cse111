age = int(input("Please enter your age: "))

heart_rate = 220 - age

low = int(heart_rate * .65)
high = int(heart_rate * .85)

print(f"When you exercise to strengthen your heart, you should keep your heart rate between {low} and {high} beats per minute.")
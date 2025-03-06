from datetime import datetime

current_date_and_time = datetime.now()

day_of_week = current_date_and_time.weekday()

# print(day_of_week)

# day_of_week = 2

subtotal = float(input("Please enter the subtotal: "))

# stretch 1
add_purchase = 50 - subtotal

if subtotal < 50:
  print(f"Your subtotal is {subtotal}. To get a 10% discount on a Tuesday or a Wednesday, please make an additional purchase of over ${add_purchase}.")

discount = 0

if (day_of_week == 1 or day_of_week == 2) and subtotal >= 50:
  discount = subtotal * .10
  subtotal -= discount

sales_tax = subtotal * .06

total_due = subtotal + sales_tax

if discount > 0:
  print(f"Discount amount: ${discount:.2f}")

print(f"Sales tax amount: ${sales_tax:.2f}")
print(f"Total amount due: ${total_due:.2f}")
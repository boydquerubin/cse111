import math

manufactured_items = int(input("Enter the number of items: "))

items_pbox = int(input("Enter the number of items per box: "))

n_box = math.ceil(manufactured_items / items_pbox)

print(f"For {manufactured_items} items, packing {items_pbox} items in each box, you will need {n_box} boxes")
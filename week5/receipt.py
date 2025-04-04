# Import the datetime class from the datetime
# module so that it can be used in this program.
from datetime import datetime, timedelta
# Call the now() method to get the current
# date and time as a datetime object from
# the computer's operating system.
current_date_and_time = datetime.now()
# Use an f-string to print the current
# day of the week and the current time.

return_by = current_date_and_time + timedelta(days=30)

import csv

PRODUCT_ID = 0
PRODUCT_QUANTITY = 1

PRODUCT_NAME_INDEX = 1
PRODUCT_PRICE_INDEX = 2


def main():
    try:
        KEY_COLUMN_INDEX = 0
        products_dict = read_dictionary("products.csv", KEY_COLUMN_INDEX)
        print("Albertsons")
        # print("All Products")
        # print(products_dict)
        # print("Requested Items:")    

        with open("request.csv", "rt") as request_file:
            reader = csv.reader(request_file)
            next(reader)

            items = 0
            subtotal = 0             

            for row_list in reader:
                product_number = row_list[PRODUCT_ID]
                quantity = int(row_list[PRODUCT_QUANTITY])

                if product_number in products_dict:
                    product_info = products_dict[product_number]
                    product_name = product_info[PRODUCT_NAME_INDEX]
                    product_price = float(product_info[PRODUCT_PRICE_INDEX])

                    total_item_price = product_price * quantity

                    print(f"{product_name}: {quantity} @ ${product_price:.2f}")
                else:
                    print(f"Warning: Product ID '{product_number}' not found in product list.")

                if quantity > 0:
                    items += quantity

                if product_price > 0:
                    subtotal += total_item_price
                    tax = subtotal * .06
                    grand_total = subtotal + tax    
            
        print(f"Number of items: {items}")
        print(f"Subtotal: ${subtotal:.2f}")
        print(f"Tax: ${tax:.2f}")
        print(f"Total: ${grand_total:.2f}")
        print("Thank you for shopping at Albertsons.")
        print(f"{current_date_and_time:%c}")
        # Exceeding the requirements
        print(f"Return by date: {return_by:%a %b %d %Y} at 9:00PM")

    except FileNotFoundError as not_found_err:
        print(not_found_err)

    except PermissionError as perm_err:
        print(perm_err)

    except KeyError as key_err:
        print(type(key_err).__name__, key_err)

def read_dictionary(filename, key_column_index):
    """
    Read the contents of a CSV file into a compound
    dictionary and return the dictionary.
    Parameters
    filename: the name of the CSV file to read.
    key_column_index: the index of the column
    to use as the keys in the dictionary.
    Return: a compound dictionary that contains
    the contents of the CSV file.
    """
    product_dictionary = {}
    with open(filename, "rt") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for row_list in reader:
            if len(row_list) != 0:
                key = row_list[key_column_index]   
                product_dictionary[key] = row_list
    return product_dictionary

if __name__ == "__main__":
    main()

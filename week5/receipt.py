import csv

PRODUCT_ID = 0
PRODUCT_QUANTITY = 1

PRODUCT_NAME_INDEX = 1
PRODUCT_PRICE_INDEX = 2


def main():
    KEY_COLUMN_INDEX = 0
    products_dict = read_dictionary("products.csv", KEY_COLUMN_INDEX)
    print("All Products")
    print(products_dict)
    print("Requested Items:")

    with open("request.csv", "rt") as request_file:
        reader = csv.reader(request_file)
        next(reader)

        for row_list in reader:
            product_number = row_list[PRODUCT_ID]
            quantity = int(row_list[PRODUCT_QUANTITY])

            if product_number in products_dict:
                product_info = products_dict[product_number]
                product_name = product_info[PRODUCT_NAME_INDEX]
                product_price = float(product_info[PRODUCT_PRICE_INDEX])

                print(f"{product_name}: {quantity} @ ${product_price:.2f}")
            else:
                print(f"Warning: Product ID '{product_number}' not found in product list.")
                
    print(f"{request_file}")

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
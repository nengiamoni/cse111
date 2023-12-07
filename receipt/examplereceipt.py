import csv
from datetime import datetime

def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    compound_dict = {}
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)  # Skip the header row
        for row in reader:
            key = row[key_column_index]
            compound_dict[key] = row
    return compound_dict

def main():
    # Call read_dictionary function for products.csv with the full path
    products_dict = read_dictionary(r'C:\Users\admin\Desktop\CSE111\receipt\products.csv', 0)

    # Print the products_dict for verification
    print("All Products")
    print(products_dict)

    # Open request.csv for reading with the full path
    with open(r'C:\Users\admin\Desktop\CSE111\receipt\request.csv', 'r') as request_file:
        reader = csv.reader(request_file)
        next(reader)  # Skip the header row

        print("\nRequested Items")
        # Process each row in the request.csv file
        for row in reader:
            product_number = row[0]
            quantity = int(row[1])

            # Check if the product number exists in products_dict
            if product_number in products_dict:
                product_info = products_dict[product_number]
                product_name = product_info[1]
                product_price = float(product_info[2])
                
                # Print each requested item separately
                print(f"{product_name}: {quantity} @ ${product_price:.2f}")

if __name__ == "__main__":
    main()

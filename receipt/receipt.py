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

    try:
        with open(filename, 'rt') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row

            for row in reader:
                key = row[key_column_index]
                value = row
                compound_dict[key] = value

    except FileNotFoundError:
        print(f"No such file or directory: '{filename}'")
        return None

    return compound_dict


def apply_discount(price, discount):
    return price * (1 - discount)


def main():
    try:
        # Call read_dictionary function to get the products dictionary
        products_dict = read_dictionary(r'C:\Users\admin\Desktop\CSE111\receipt\products.csv', 0)

        if products_dict is None:
            return

        # Get the current day of the week (0 = Monday, 1 = Tuesday, ..., 6 = Sunday)
        current_day = datetime.now().weekday()

        # Define the discount rate
        discount_rate = 0.1  # 10%

        # Check if today is Tuesday or Wednesday
        apply_discount_flag = current_day == 1 or current_day == 2

        print("current day is Tue/Wed ? ----",  apply_discount_flag)

        # Print the store name at the top of the receipt
        print("\nStore Name: Bishop Stores\n")

        # Open the request.csv file for reading
        with open(r'C:\Users\admin\Desktop\CSE111\receipt\request.csv', 'r') as request_file:
            reader = csv.reader(request_file)
            next(reader)  # Skip header row

            total_items = 0
            subtotal = 0.0

            # Process each row in the request.csv file
            for row in reader:
                product_number = row[0]

                # Check if the product_number exists in products_dict
                # if product_number in products_dict:
                product_info = products_dict[product_number]
                product_name = product_info[1]
                quantity = int(row[1])
                price = float(product_info[2])

                # Print product details using f-string
                print(
                    f"✅ {product_name}, Quantity: {quantity}, Price: ${price:.2f}")
                # Update total items and subtotal
                total_items += quantity
                subtotal += quantity * price

            # Print the list of ordered items
            print("\nOrdered Items:")
            print(f"Total Items: {total_items}")

            # Print the sum of the number of ordered items
            print(f"Subtotal: ${subtotal:.2f}")

            # Apply discount if today is Tuesday or Wednesday
            if apply_discount_flag:
                print("You've got 10% discount!")
                subtotal = apply_discount(subtotal, discount_rate)
                print(f"Subtotal after discount: ${subtotal:.2f}")

            # Compute and print sales tax
            sales_tax_rate = 0.06
            sales_tax = subtotal * sales_tax_rate
            print(f"Sales Tax (6%): ${sales_tax:.2f}")

            # Compute and print total amount due
            total_due = subtotal + sales_tax

            print(f"Total Amount Due: ${total_due:.2f}")

            # Print a thank you message
            print("\nThank you for shopping with us at Bishop Stores!")

            # Get the current date and time
            current_datetime = datetime.now().strftime("%a %b %d %H:%M:%S %Y")
            print(current_datetime)

    except KeyError as e:
        print(f"Unknown product ID in the request.csv file - {e}")


if __name__ == "__main__":
    main()

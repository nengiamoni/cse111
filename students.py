import csv


def read_dictionary(filename, key_column_index=None):
    # Read the contents of a CSV file into a dictionary or a compound dictionary and return the dictionary.

    # Create an empty dictionary that will store the data from the CSV file.
    dictionary = {}

    # Open the CSV file for reading and store a reference to the opened file in a variable named csv_file.
    with open(filename, "rt") as csv_file:

        # Use the csv module to create a reader object that will read from the opened CSV file.
        reader = csv.reader(csv_file)

        # The first row of the CSV file contains column headings and not data, so this statement skips the first row of the CSV file.
        next(reader)

        # The reader object returns each row as a list. Read the rows in the CSV file one row at a time.
        for row in reader:
            if len(row) != 0:

                # Determine the key based on the provided index or use the first column as the key if index is None.
                if (key_column_index) is not None:
                    key = row[key_column_index]
                else:
                    key = row[0]

                # Store the data from the current row into the dictionary.
                dictionary[key] = row[1:]

    return dictionary


def main():

    # Read the contents of the students.csv file into a dictionary.
    students_dictionary = read_dictionary("students.csv")

    i_number = input("Enter I-Number: ")

    # Remove dashes from the entered I-Number.
    i_number = i_number.replace("-", "")

    # Validate the I-Number.
    if not i_number.isdigit():
        print("Invalid I-Number")
        return

    # Use the I-Number to find the corresponding student name in the dictionary.
    student_name = students_dictionary.get(i_number)

    if student_name is not None:
        print(f"Student Name: {student_name[0]}")
    else:
        print("No such student.")


if __name__ == "__main__":
    main()

#Global variables to be called inside different functions
code= 0
name=0
unit_price=0
quantity=0
total_price=0




# Function to read inputs from a file
def read_inputs_from_file(products):
    # Open the file in read mode
    file = open(products, "r")
    # Read all lines from the file and store them in a list
    inputs= file.readlines()
    # Return the list of inputs
    return inputs


# Function to print to a screen and an external file
def print_to_screen_and_file(text, screen, file):
    print(text, file=file)
    print(text)


# Function to create a product database
def create_product_database():
    # Create an empty dictionary to store the product database
    product_db = {}
    # Iterate over each line from the input file
    for line in read_inputs_from_file("products.txt"):
        # Split the line by comma to extract individual values
        product_code, product_name, product_price, product_stock = line.split(",")
        # Create a dictionary for each product and store its information
        product_db[product_code] = {
            "name": product_name,
            "price": float(product_price),
            "stock": int(product_stock),
        }
    # Return the product database dictionary
    return product_db


# Function to display the product menu
def display_menu(product_db):
    print("Product Code\tProduct Name\tPrice\tStock")
    # Iterate over the product database dictionary
    for code, values in product_db.items(): #loop on keys and its values
        # Print the product details
        print(f"{code}\t\t\t\t {values['name']}\t\t\t{values['price']}\t\t{values['stock']}")
    print("* Press 2 to process order\n")

# Function to process an order
def process_order(product_db):
    global code,name,unit_price,quantity,total_price

    code = input("Enter product code: ")
    # Update the name and unit_price global variables based on the entered code
    name = product_db[code]["name"] # updating global variables after taking the code
    unit_price = product_db[code]["price"] # updating global variables after taking the code
    #check if the code is found in database
    if code not in product_db:
        print("Invalid product code")
        return
    #check if there is enough amount products in stock to process with
    quantity = int(input("Enter quantity: "))
    if quantity > product_db[code]["stock"]:
        print("Insufficient stock")
        return
    #printing the total price of product
    total_price = quantity * product_db[code]["price"]
    product_db[code]["stock"] -= quantity

    # Update the quantity in the file (product.txt) for the corresponding code
    lines = read_inputs_from_file("products.txt")
    for i in range(len(lines)):
        product_line = lines[i].split(",")
        if product_line[0] == code:
            product_line[3] = str(product_db[code]["stock"])
            lines[i] = ",".join(product_line)+ "\n"
            break
    # Open the file in write mode to update the quantity
    file = open("products.txt", "w")
    for line in lines:
        file.write(line)
    file.close()

    print(f"\nTotal price: {total_price}\n* Press 3 to generate receipt\n")


# Function to generate a receipt
def generate_receipt():
    #calling the global variables that are defined before
    global code,name,unit_price,quantity,total_price
    print("Receipt:")
    print("Code\t\tProduct Name\t\tUnit Price\t\tQuantity")
    print(f"{code}\t\t\t{name}\t\t\t\t{unit_price}\t\t\t\t{quantity}\n")
    print(f"                       \t\t\tReceipt Total \t{total_price}")

    print("Thank you for shopping with us!\n")


# Function to main menu
def main_menu():
    # the list to choose from
    while True:
        print("1. Display menu")
        print("2. Process order")
        print("3. Generate receipt")
        print("4. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            display_menu(product_db)
        elif choice == 2:
            process_order(product_db)
        elif choice == 3:
            generate_receipt()
        elif choice == 4:
            break


if __name__ == "__main__":
    # calling the database to be used in other functions
    product_db = create_product_database()
    main_menu()

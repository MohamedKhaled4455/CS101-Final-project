#Global variables to be called inside different functions
code= 0
name=0
unit_price=0
quantity=0
total_price=0




# Function to read inputs from a file
def read_inputs_from_file(products):
    file = open(products, "r")
    inputs= file.readlines()
    return inputs


# Function to print to a screen and an external file
def print_to_screen_and_file(text, screen, file):
    print(text, file=file)
    print(text)


# Function to create a product database
def create_product_database():
    product_db = {}
    for line in read_inputs_from_file("products.txt"):
        product_code, product_name, product_price, product_stock = line.split(",")
        product_db[product_code] = {
            "name": product_name,
            "price": float(product_price),
            "stock": int(product_stock),
        }
    return product_db


# Function to display the product menu
def display_menu(product_db):
    print("Product Code\tProduct Name\tPrice\tStock")
    for code, values in product_db.items(): #loop on keys and its values
        print(f"{code}\t\t\t\t {values['name']}\t\t\t{values['price']}\t\t{values['stock']}")


# Function to process an order
def process_order(product_db):
    global code,name,unit_price,quantity,total_price

    code = input("Enter product code: ")
    name = product_db[code]["name"] # updating global variables after taking the code
    unit_price = product_db[code]["price"] # updating global variables after taking the code

    if code not in product_db:
        print("Invalid product code")
        return

    quantity = int(input("Enter quantity: "))
    if quantity > product_db[code]["stock"]:
        print("Insufficient stock")
        return

    total_price = quantity * product_db[code]["price"]
    product_db[code]["stock"] -= quantity
    #add editing quantitiy on the file
    print(f"Total price: {total_price}")


# Function to generate a receipt
def generate_receipt():
    global code,name,unit_price,quantity,total_price
    print("Receipt:")
    print("Code\t\tProduct Name\t\tUnit Price\t\tQuantity")
    print(f"{code}\t\t\t{name}\t\t\t\t{unit_price}\t\t\t\t{quantity}\n")
    print(f"                       \t\t\tReceipt Total \t{total_price}")

    print("Thank you for shopping with us!")


# Function to main menu
def main_menu():
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
    product_db = create_product_database()
    main_menu()

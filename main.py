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
    for code, product in product_db.items():
        print(f"{code}\t{product['name']}\t\t{product['price']}\t{product['stock']}")


# Function to process an order
def process_order(product_db):
    code = input("Enter product code: ")
    if code not in product_db:
        print("Invalid product code")
        return

    quantity = int(input("Enter quantity: "))
    product = product_db[code]
    if quantity > product["stock"]:
        print("Insufficient stock")
        return

    total_price = quantity * product["price"]
    product["stock"] -= quantity
    print(f"Total price: {total_price}")


# Function to generate a receipt
def generate_receipt(product_db):
    print("Receipt:")
    for code, product in product_db.items():
        if product["stock"] < 10:
            print(f"{product['name']} ({code}): {product['stock']} left")
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
            generate_receipt(product_db)
        elif choice == 4:
            break


if __name__ == "__main__":
    product_db = create_product_database()
    main_menu()

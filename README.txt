Product Ordering System

This program is a simple product ordering system that allows users to display a menu, process orders, generate receipts, and update the product database.

Functionality:
1. Display menu: Shows the available products with their codes, names, prices, and stock quantities.
2. Process order: Allows the user to enter a product code and quantity to place an order. It checks the availability of the product and updates the stock quantity accordingly.
3. Generate receipt: Generates a receipt for the last processed order, displaying the product code, name, unit price, quantity, and the total price.
4. Exit: Terminates the program.
5- 'GUI'

Files:
- `products.txt`: Contains the product information in the format "code,name,price,stock". Each product is listed on a separate line.
- `main.py`: The main Python script that implements the product ordering system.
- 'run_in_cmd': provides the option to function file 'main.py', but in cmd
- 'GUI': make easier for the user to function the main code file with simpler interface

Usage:
1. Make sure the `products.txt` file is present and contains the correct product information.
2. Run the `main.py` script using a Python interpreter.
3. Follow the on-screen prompts to navigate through the product ordering system.
4. After each order is processed, the product database is updated, and the receipt is displayed.

Note: -This program assumes that the `products.txt` file is in the same directory as the `main.py` script. If the file or its format is modified, ensure the changes are made accordingly.


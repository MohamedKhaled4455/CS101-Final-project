from tkinter import *

class ProductOrderingSystem:
    def __init__(self, master):
        self.master = master
        master.title("Product Ordering System")

        # Menu Label
        self.menu_label = Label(master, text="Menu")
        self.menu_label.grid(row=0, column=0)

        # Menu Listbox
        self.menu_listbox = Listbox(master, height=10, width=30)
        self.menu_listbox.grid(row=1, column=0)
        self.menu_items = ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"]
        for item in self.menu_items:
            self.menu_listbox.insert(END, item)

        # Order Label
        self.order_label = Label(master, text="Order")
        self.order_label.grid(row=0, column=1)

        # Order Listbox
        self.order_listbox = Listbox(master, height=10, width=30)
        self.order_listbox.grid(row=1, column=1)

        # Add Button
        self.add_button = Button(master, text="Add >>", command=self.add_item)
        self.add_button.grid(row=2, column=0)

        # Remove Button
        self.remove_button = Button(master, text="<< Remove", command=self.remove_item)
        self.remove_button.grid(row=2, column=1)

        # Generate Receipt Button
        self.receipt_button = Button(master, text="Generate Receipt", command=self.generate_receipt)
        self.receipt_button.grid(row=3, column=1)

        # Update Database Button
        self.update_button = Button(master, text="Update Database", command=self.update_database)
        self.update_button.grid(row=3, column=0)

    def add_item(self):
        selected_item = self.menu_listbox.get(self.menu_listbox.curselection())
        if selected_item not in self.order_listbox.get(0, END):
            self.order_listbox.insert(END, selected_item)

    def remove_item(self):
        selected_item = self.order_listbox.get(self.order_listbox.curselection())
        self.order_listbox.delete(self.order_listbox.curselection())

    def generate_receipt(self):
        selected_items = self.order_listbox.get(0, END)
        receipt = ""
        for item in selected_items:
            receipt += item + "\n"
        messagebox.showinfo("Receipt", receipt)

    def update_database(self):
        messagebox.showinfo("Update Database", "Database Updated Successfully!")

root = Tk()
product_ordering_system = ProductOrderingSystem(root)
root.mainloop()

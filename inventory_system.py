import os
import json

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class InventorySystem:
    def __init__(self, file_name="inventory.json"):
        self.file_name = file_name
        if not os.path.exists(self.file_name):
            with open(self.file_name, 'w') as file:
                json.dump([], file)

    def load_products(self):
        with open(self.file_name, 'r') as file:
            return json.load(file)

    def save_products(self, products):
        with open(self.file_name, 'w') as file:
            json.dump(products, file)

    def add_product(self, product):
        products = self.load_products()
        for p in products:
            if p['name'] == product.name:
                print("Product already exists.")
                return
        products.append(product.__dict__)
        self.save_products(products)
        print("Product added successfully!")

    def delete_product(self, product_name):
        products = self.load_products()
        products = [p for p in products if p['name'] != product_name]
        self.save_products(products)
        print("Product deleted successfully!")

    def list_products(self):
        products = self.load_products()
        if not products:
            print("No products available.")
        else:
            for p in products:
                print(f"Name: {p['name']}, Price: {p['price']}, Quantity: {p['quantity']}")

if __name__ == "__main__":
    inventory = InventorySystem()

    while True:
        action = input("What do you want to do? (add / delete / list / exit): ").lower()
        if action == "add":
            name = input("Product name: ")
            price = float(input("Product price: "))
            quantity = int(input("Product quantity: "))
            product = Product(name, price, quantity)
            inventory.add_product(product)
        elif action == "delete":
            name = input("Product name to delete: ")
            inventory.delete_product(name)
        elif action == "list":
            inventory.list_products()
        elif action == "exit":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

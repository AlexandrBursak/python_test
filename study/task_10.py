class Products:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def sell_product(self, number):
        if number <= self.quantity:
            self.quantity -= number
        else:
            raise Exception
    
    def __str__(self):
        return f"Product: Name {self.name}, Price: {self.price}, Qty: {self.quantity}"


class Inventory:

    def __init__(self):
        self.products = []

    def add_product(self, product: Products):
        self.products.append(product)
    
    def __str__(self):
        result = ""
        for item in self.products:
            result += f"{item}\n"
        return result
    

def main():
    inventory = Inventory()

    inventory.add_product(Products("Apple", 10, 10))
    inventory.add_product(Products("Pear", 5, 15))
    inventory.add_product(Products("Orange", 6, 7))

    print("Initial Inventory")
    print(inventory)

    inventory.products[0].sell_product(5)
    inventory.products[1].sell_product(20)

    print(inventory)


if __name__ == "__main__":
    main()
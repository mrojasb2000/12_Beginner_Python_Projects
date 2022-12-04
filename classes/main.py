class Item:
    
    def __init__(self, name):
        print(f"An instance created: {name}")

    def calculate_total_price(self):
        return self.price * self.quantity

item1 = Item("Phone")
#print(item1.calculate_total_price())

item2 = Item("Laptop")
#print(item2.calculate_total_price())

# Get type
#print(type(item1))
#print(type(item1.name))
#print(type(item1.price))
#print(type(item1.quantity))
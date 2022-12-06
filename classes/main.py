class Item:
    
    def __init__(self, name: str, price: float, quantity: int = 0):
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greate or equal to than zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greate or equal than zero!"
         
        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity

item1 = Item("Phone", 100, 1)
print(item1.calculate_total_price())

item2 = Item("Laptop", 1000, 3)
item2.has_numpad = False
print(item2.calculate_total_price())

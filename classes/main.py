class Item:
    pay_rate = 0.8 # The pay after 20% discount
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

    def apply_discount(self):
        self.price *= Item.pay_rate

item1 = Item("Phone", 100, 2)
print(f"Total price : $ {item1.calculate_total_price()}")
item1.apply_discount()
print(f"Price with {1 - item1.pay_rate:.2f}% discount : $ {item1.price}")

#item2 = Item("Laptop", 1000, 3)
#item2.has_numpad = False
#print(item2.calculate_total_price())
#
## All the attributes from class level
#print(Item.__dict__)
## All the attributes from instance level
#print(item1.__dict__)

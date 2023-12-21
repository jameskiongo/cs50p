class Item:
    pay_rate = 0.8 #pay after 20% discount
    all = []
    def __init__(self, name: str, price: float, quantity=0):
        # validation
        assert price >= 0, f"Price {price} is less than 0!"
        assert quantity >= 0, f"Quantity {quantity} is less than 0!"

        self.name = name
        self.price = price
        self.quantity = quantity
        
        #execute
        Item.all.append(self)
    def calculate_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate

    def __repr__(self):
        return f"Item('{self.name}', '{self.price}', '{self.quantity}')"

item1 = Item("phone", 100, 5)
item2 = Item("laptop", 1000, 3)
item3 = Item("cable", 10, 5)
item4 = Item("mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)

print(Item.all)
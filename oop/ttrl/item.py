import csv 

class Item:
    all = []
    def __init__(self, name: str, price: float, quantity=0):
        # validation
        assert price >= 0, f"Price {price} is less than 0!"
        assert quantity >= 0, f"Quantity {quantity} is less than 0!"

        self.__name = name
        self.price = price
        self.quantity = quantity
        
        #execute
        Item.all.append(self)

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        self.__name = value

    def calculate_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate
    
    @classmethod
    def instantiate_csv(cls):
        with open("items.csv", "r") as file:
            reader = csv.DictReader(file)
            items = list(reader)
        for item in items:
            Item(
                name = item.get("name"),
                price = float(item.get("price")),
                quantity = int(item.get("quantity")),
            )

    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', '{self.price}', '{self.quantity}')"

    
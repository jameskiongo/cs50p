from item import Item

class Phone(Item):
    def __init__(self, name: str, price: float, quantity=0, broken_phone=0):
        #super function to access all attributes
        super().__init__(
            name, price, quantity
        )
        
        # validation
        assert broken_phone >= 0, f"Broken phone {broken_phone} is less than 0!"

        
        self.broken_phone = broken_phone
        
    
class Jar:
    def __init__(self, capacity=12):
        self.__capacity = capacity
        self.__size = 0

    def __str__(self):
        return "🍪" * self.__size

    def deposit(self, n):
        if self.__size > self.__capacity:
            raise ValueError 
        self.__capacity += n

    def withdraw(self, n):
        if self.__size > self.__capacity:


    @property
    def capacity(self):
        if self.capacity < 0:
            raise ValueError
        return self.__capacity

    @property
    def size(self):
        return self.__size

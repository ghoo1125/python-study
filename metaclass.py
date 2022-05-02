class MyMeta(type):
    def __new__(cls, name, bases, dict):
        # Add HaHa prefix before every class name, and remove all attributes
        return super().__new__(cls, "HaHa"+name, bases, {})

class SomeClass(metaclass=MyMeta):
    def __init__(self):
        self.num = 10

if __name__ == "__main__":
    # AttributeError: 'HaHaSomeClass' object has no attribute 'num'
    print(SomeClass().num)

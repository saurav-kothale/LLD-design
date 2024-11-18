class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        
        if cls._instance is None:
            print("creating new instance")
            cls._instance = super().__new__(cls)


        return cls._instance
    
    def __init__(self, value):
        print("initializing object")
        self.value = value


obj1 = Singleton(10)
obj2 = Singleton(20)

# obj3 = Singleton(30)

# print(obj1 is obj2)
print(obj1.value)
print(obj2.value)
# print(obj3.value)
from abc import abstractmethod,ABC

class House:
    def __init__(self):
        self.window = None
        self.door = None
        self.swimming = None
        self.garage = None

    def __str__(self):
        return f"House with: {self.window} windows, {self.door} doors, {self.garage}, {self.swimming}"
    

class HouseBuilder(ABC):
    @abstractmethod
    def build_window(self):
        pass

    @abstractmethod
    def build_door(self):
        pass

    @abstractmethod
    def build_swimming(self):
        pass

    @abstractmethod
    def build_garage(self):
        pass


class ConcreteHouseBuilder(HouseBuilder):

    def __init__(self):
        self.house = House()

    def build_door(self):
        self.house.door = 4
        return self
    
    def build_window(self):
        self.house.window = 5
        return self
    
    def build_garage(self):
        self.house.garage = 1
        return self
    
    def build_swimming(self):
        self.house.swimming = 1
        return self  

    def get_house(self):
        return self.house
    

class DirectorHouse:
    def __init__(self, builder):
        self.builder = builder

    def construct_house(self):
        self.builder.build_window().build_door().build_garage().build_swimming()
        return self.builder.get_house()
    

builder = ConcreteHouseBuilder()
director = DirectorHouse(builder)
house = director.construct_house()
print(house)

class IAnimal:
    def speak(self):
        pass

    def type(self):
        pass

class Cat(IAnimal):
    def speak(self):
        return "Meow"
    
    def type(self):
        return "Cat"
    
class Dog(IAnimal):
    def speak(self):
        return "Bark"
    
    def type(self):
        return "DOG"
    
class Shark(IAnimal):
    def speak(self):
        return "Cannot speak"
    
    def type(self):
        return "Shark"
    
class Octopus(IAnimal):
    def speak(self):
        return "Squawck"
    
    def type(self):
        return "Octopus"
       

class AnimalFactory:
    def __init__(self):
        pass

    def get_animal(self, animal_type):
        raise NotImplementedError
    

    @staticmethod
    def create_animal_factory(factory_type):
        if factory_type == "Sea":
            return SeaAnimalFactory()
        
        elif factory_type == "Land":
            return LandAnimalFactory()
        
        else:
            print("Land animal type not supported!")
            return None

class LandAnimalFactory(AnimalFactory):
    def get_animal(self, animal_type):
        if animal_type == "cat":
            return Cat()
        
        elif animal_type == "dog":
            return Dog()
        
        else:
            print("Land animal type not supported!")
            return None
        

class SeaAnimalFactory(AnimalFactory):
    def get_animal(self, animal_type):
        if animal_type == "Shark":
            return Shark()
        
        elif animal_type == "Octopus":
            return Octopus()
        
        else:
            print("Sea animal type not supported!")
            return None
        



        

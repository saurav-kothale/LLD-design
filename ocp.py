from abc import ABC, abstractmethod

class Employee(ABC):
    
    def __init__(self, name : str, salary : str):
        self.name = name
        self.salary = salary

    
    @abstractmethod
    def work(self):
        pass


class Tester(Employee):

    def __init__(self, name: str, salary: str):
        super().__init__(name, salary)

    
    def test(self):
        print("{} is testing".format(self.name))

    def work(self):
        self.test()

    
class Develop(Employee):

    def __init__(self, name: str, salary: str):
        super().__init__(name, salary)

    def developed(self):
        print("{} is developing".format(self.name))

    def work(self):
        self.developed()


class Company:

    def __init__(self, name : str):
        self.name = name

    def work(self, employee : Employee):
        employee.work()


company = Company("carbon")
developer = Develop("Nusret", "1000000")
tester = Tester("Someone", "1000000")

company.work(developer)
company.work(tester)


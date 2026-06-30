# inheritance and advance OPP

# Animal is-a object (yes, sort of confusing) look at the extra credit

class Animals(object):
    pass

class Dog(Animals):
    def __init__(self,name):
        self.name= name

class Cats(Animals):
    def __init__(self,name):
        self.name= name


class Person(object):
      def __init__(self,name):
        self.name= name
        # Person has-a pet of some kind
        self.pet = None

class Employee(Person):
    def __init__(self, name, salary,):
        # ?? hmm what is this strange magic
        super(Employee, self).__init__(name)
        self.salary = salary

class Fish(object):
    pass
class salmon(Fish):
    pass
class Halibut(Fish):
    pass

## rover is-a Dog
rover= Dog("Rover")
satan = Cats("Satan")
mary = Person("Mary")
mary.pet = satan
frank = Employee("Frank", 120000)
frank.pet = rover
flipper = Fish()
crouse = salmon()
harry = Halibut()

print(rover.name)
print(satan.name)
print(mary.name)
print(mary.pet.name)
print(frank.name)
print(frank.salary)
print(frank.pet.name)
print(flipper)
print(crouse)
print(harry)
# basic object-oriented programming
# Basic Object-Oriented Programming (OOP) ka matlab hai data (attributes) aur us par kaam karne wale functions (methods) ko ek class ke andar organize karna, aur us class se objects bana kar unka use karna.
# __init__ constructor hai, jo object bante hi automatically chalta hai aur object ki initial values set karta hai.
# self current object ko represent karta hai.
class Person(object):
    def __init__(self,name,age,eyes):
        self.name = name
        self.age = age
        self.eyes = eyes
    
    def talk(self, words):
        print(f"i am {self.name} and {words}")

becky = Person("hitesh", 18, "blue")
becky.talk("I am talking here!")

# using dir() and __dict__
# .__dict__ ek special attribute hai jo kisi object ya class ke saare attributes ko dictionary ke form me dikhata hai.
becky = Person("Becky", 39, "green")
print(becky.__dict__)

#  the class that becky comes from
# __class__ ek special attribute hai jo batata hai ki ye object kis class se bana hai.
print(becky.__class__)

# the contents of that class
# Is object ke andar kya-kya available hai?" ye dir() batata hai.
print(dir(becky))

# these two do the same thing
# ek built-in Python function hai jo kisi object ka attribute ya method uske naam (string) se access karta hai.
print(becky.talk)
print(getattr(becky, 'talk'))

# this is the class's version of talk
print(becky.__class__.__dict__['talk'])

# about the dot(.)
becky = Person("Becky", 39, "green")
becky.talk("I am talking here!")

# a word "self" this very important why he  _init_ use in this self is very beneficiall
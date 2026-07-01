# inharitance versus composition
# 🧬 Inheritance (विरासत लेना)
# Jab ek class dusri class ki properties aur functions le leti hai.
# Composition (banakar use karna)
# Jab ek class ke andar dusri class ka object use hota hai.
# implicit inharitnace
# class Parent(object):
#     def implicit(self):
#         print("implicit()")
# class Child(Parent):
#     pass

# dad = Parent()
# son = Child()

# dad.implicit()
# son.implicit()


# override explicity
# class Parent(object):
#     def override(self):
#         print("Parent")
# class Child(Parent):
#     def override(self):
#         print("child")

# dad = Parent()
# son = Child()

# dad.override()
# son.override()

# alter before or after
# class Parent(object):
#     def altered(self):
#         print("PARENT altered()")
# class Child(Parent):
#  def altered(self):
#     print("CHILD, BEFORE PARENT altered()")
#     super(Child,self).altered()
#     print("CHILD, AFTER PARENT altered()")

# dad = Parent()
# son = Child()

# dad.altered()
# son.altered()

# all three in one

# class Parent(object):

#     def override(self):
#         print("PARENT override()")

#     def implicit(self):
#         print("PARENT implicit()")

#     def altered(self):
#         print("PARENT altered()")


# class Child(Parent):

#     def override(self):
#         print("CHILD override()")

#     def altered(self):
#         print("CHILD, BEFORE PARENT altered()")
#         super(Child, self).altered()
#         print("CHILD, AFTER PARENT altered()")


# dad = Parent()
# son = Child()

# dad.implicit()
# son.implicit()

# dad.override()
# son.override()

# dad.altered()
# son.altered()

class Other(object):

    def override(self):
        print("OTHER override()")

    def implicit(self):
        print("OTHER implicit()")

    def altered(self):
        print("OTHER altered()")


class Child(object):

    def __init__(self):
        self.other = Other()

    def implicit(self):
        self.other.implicit()

    def override(self):
        print("CHILD override()")

    def altered(self):
        print("CHILD, BEFORE OTHER altered()")
        self.other.altered()
        print("CHILD, AFTER OTHER altered()")


son = Child()

son.override()
son.implicit()
son.altered()
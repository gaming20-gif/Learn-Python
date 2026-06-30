# Names, Variable, Code, Functions

# e1  =
# def do_nothing():
#     pass
# def creates the function, but the pass keyword tells Python this function is empty.

# e2 = 
# def do_spmething():
#     print("i did something")

# do_spmething()
# this function is runnibg right but you call functions position is line start

# e3 = 
# def do_more_thing(a, b):
#     print("A is", a ,"and", "B is", b)
# do_more_thing("hello", 1)

# e4 = 
# def do_more_things(a, b):
#     a = "hello"
#     b = 1
#     # print("A IS", a, "B IS", b)   #not shaw err0r
# print("A IS", a, "B IS", b)   #saw error why = argument is not chnageble

# e5= 
# this one is like your scripts with argv

def print_two(*args):
     arg1, arg2 = args
     print(f"arg1: {arg1}, arg2: {arg2}")

# ok, that *args is actually pointless, we can just do this
def print_two_arg(arg1,arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# up to are same but in deffrant way


# this just takes one argument
def print_one_arg(arg1):
    print(f"arg1: {arg1}")

# this one takes no arguments
def print_none():
   print("I got nothin.")

print_two("one", "two")
print_two_arg("one", "two")
print_one_arg("one")
print_none()



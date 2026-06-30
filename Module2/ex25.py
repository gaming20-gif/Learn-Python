# dictionaries and functions
def print_number(x):
 print("NUMBER IS", x)

rename_print = print_number
# first 1
rename_print(100)
# second 2
print_number(100)


# coler save variable
color = "Red"
# then i create object and make key for color and save it
corvette = {
 "color": color
 }
# then print color use object  and add key
print("LITTLE", corvette["color"], "CORVETTE")


def run():
 print("Vroom")

corvette = {
 "color": "red",
 "run" : run
 }
print( "shoe color is", corvette["color"])
# function run
corvette["run"]()


myRun = corvette["run"]
myRun()
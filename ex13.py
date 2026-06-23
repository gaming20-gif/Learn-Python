# paramereters, unpacking, variables
from sys import argv
script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

# python ex13.py apple mango banana - this run in python code show All

# sys Python का built-in module है।
# argv = argument vector
# यह command line से दिए गए arguments को list के रूप में रखता है।
# argv क्या है?
# जब तुम Python file चलाते हो, तो file के नाम के बाद कुछ extra values दे सकते हो।
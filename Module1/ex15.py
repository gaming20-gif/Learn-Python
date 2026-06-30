# argv से filename लेना
# open() से file खोलना
# .read() से file पढ़ना
# input() से user से filename लेना
# Extra Experiment
from sys import argv
script, filename = argv
# file name ans open it
txt = open(filename)
print(f"Here's your file {filename}:")
# in ex test.txt read all content
print(txt.read())
print("Type the filename again:")
# tyoe
file_again = input("> ")
# again type file name like test.txt
txt_again = open(file_again)
# then read content and saw his content
print(txt_again.read())

# python ex15.py test.txt
# test.txt



from sys import argv
from os.path import exists

from_file = "test.txt"
to_file = "new_test.txt"

print(f"copying from {from_file} to {to_file}")

in_file = open(from_file)
in_data = in_file.read()

print(f"the input file is {len(in_data)} bytes long")
print("Ready, hit RETURN to continue, CTRL-C to abort.")

input()

out_file = open(to_file, "w")
out_file.write(in_data)

print("Alright, all done.")

in_file.close()
out_file.close()
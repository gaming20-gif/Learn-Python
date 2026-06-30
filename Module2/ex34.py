# while loop
i = 0
numbers = []

while 1 < 6:
    print(f"at the top i is {i}")
    numbers.append(i)
    i = i + 1
    
    # print("numbers now :", numbers)
    print(f"At the bottom i is {i}")

# print("The numbers: ")
# for num in numbers:
#     print(num)



# from dis import dis

# dis('''
#  i = 0
#  while i < 6:
#  i = i + 1
#  ''')
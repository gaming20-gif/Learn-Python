# loops and list
# for in loop
the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']
for number in the_count:
    print(f"show number {number}")
for fruit in fruits:
    print(f"how many {fruit} in the bascket")
for i in change:
    print(f"I got {i}")


# 


elements= []
# useing range for for number liek i add number 0 to 6  to shaw 0 1 2 3 4 5 show six number 
for i in range(1,6):
    print(f"range is {i}")
    elements.append(i)

# for i in elements:
#     print(f"Element was: {i}")

# 
# from dis import dis
# dis('''
#   for number in the_count:
#    print(number)
#    ''')
# introductory lists

fruit = [
    ['Apples', 12, 'AAA'],
    ['Oranges', 1, 'B'],
    ['Pears', 2, 'A'],
    ['Grapes', 14, 'UR']
]
# print(fruit[2][2])

cars = [
    # 0 [0                   1]
    #   [0]           [0   , 1 ,   2]
    ['Cadillac', ['Black', 'Big', 34500]], #0
    ['Corvette', ['Red', 'Little', 1000000]],  #1
    ['Ford', ['Blue', 'Medium', 1234]],  #2
    ['BMW', ['White', 'Baby', 7890]]  #3
]
print(cars[1][1][2])
# in array has sub array like covertty is one and second is red two thing
# printlike [1] =corvette
#  [1][1]= shaw [red]
#  [1][1][2] = 100000 
languages = [
    ['Python', ['Slow', ['Terrible', 'Mush']]],
    ['JavaScript', ['Moderate', ['Alright', 'Bizarre']]],
    ['Perl6', ['Moderate', ['Fun', 'Weird']]],
    ['C', ['Fast', ['Annoying', 'Dangerous']]],
    ['Forth', ['Fast', ['Fun', 'Difficult']]],
]
print(languages[1][1][1][1])
print(languages[3][1][1][0])
# fruit
# │
# ├── 0 → ['Apples', 12, 'AAA']
# ├── 1 → ['Oranges', 1, 'B']
# ├── 2 → ['Pears', 2, 'A']
# └── 3 → ['Grapes', 14, 'UR']

# 0 → Fruit name
# 1 → Quantity
# 2 → Grade
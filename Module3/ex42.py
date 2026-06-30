# doing thing to lists
# Is exercise me author sikhata hai ki Python Lists ke saath alag-alag operations kaise karte hain.
# Ab tak tumne list banana aur uske elements access karna seekha tha. Ab tum list ko modify, update aur manage karna seekhoge.

# | Method          | Kya karta hai?                                                 
# | `pop()`         | Last item remove karta hai aur return bhi karta hai.           |
# .split(' ')         ka use string ko space ke basis par alag-alag parts me todne ke liye hota hai.
# .join()            .join() ka use list ke items ko jodkar ek string banane ke liye hota hai.
# .get()              ka use dictionary se value safely nikalne ke liye hota hai.valu nahi none or aapne jo error likha vo dikhega
ten_things = "Apples Oranges Crows Telephone Light Sugar"
print("Wait there are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee",
              "Corn", "Banana", "Girl", "Boy"]
# len = length
while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    stuff.append(next_one)
    print(f"there are {len(stuff)} item now")

print("There we go: ", stuff)
print("Let's do some things with stuff.")

print(stuff[0])
print(stuff[-10])
print(stuff.pop())
# .join is convdr in string
print(' '.join(stuff)) # what? cool!
# 3 number and 5 number value print with join 
print('#'.join(stuff[3:5])) # super stellar!

# else and if
people = 30
cars = 40
dogs = 15

if cars > people:
    print("We should take the cars.")
elif cars < people:
   print("We should not take the cars.")
else:
  print("We can't decide.")

if people <= dogs:
   print("not buy")
elif people >= dogs:
  print("Buy now")
else:
 print("not decided")



from dis import dis

dis("""
cars = 100
people = 30

if cars > people:
    print("We should take the cars.")
elif cars < people:
    print("We should not take the cars.")
else:
    print("We can't decide.")
""")
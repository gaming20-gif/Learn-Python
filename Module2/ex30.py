# what if
# from dis import dis
people = 20
cats = 30
dogs = 15

if people < cats:
   print("kya cats people se jyada he", "ha")

if people > cats:
   print("kya people cats se jya de", "na")

if people < dogs:
   print("kya dogs people se jyada he", "ha")

if people > dogs:
   print("kya people dogs se jya he", "na")


dogs += 5
if people <= dogs:
   print("kya dogs people se jyada he ya uske jitne he")

if people >= dogs:
   print("kya people dogs se jya he  ya uske jitne he")

if people == dogs:
   print("kya people dogs same he", "haa")





# dis('''
#   if people < cats:
#     print("Too many cats! The world is doomed!")
#  ''')
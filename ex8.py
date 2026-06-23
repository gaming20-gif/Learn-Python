# Formatting String Menually

formetter = "{} {} {} {}"
# conditionis need four value you add three throw error
print(formetter.format(1,2,3,4))
# in the for object  i ad 5 value but saw four value
# print(formetter.format(1,2,3,4,5))

print(formetter.format("one","two","three", "four"))
print(formetter.format(True,False,False, True))
print(formetter.format(formetter,formetter,formetter,formetter,formetter))
print(formetter.format("Today Learn About","Formatting string", "Menually", "."))
# string and text

type_of_people = 10
x = f"there are {type_of_people} types of people"

binary = "binary" 
do_not = "don't"
y = f"those who kwon {binary} and those who {do_not}"
print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: {y}")

# .format() एक string method है जो string में values डालने के लिए इस्तेमाल होती है
hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"
print(joke_evaluation.format(hilarious))

name = "Hitesh"
age = 21
text = "My name is {} and I am {} years old.".format(name, age)
print(text)


w = "This is the left side of..."
e = "a string with a right side."
print(w + e)

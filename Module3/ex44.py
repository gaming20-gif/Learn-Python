# from dictionaries to object
# summery=
#   Dictionary me data store kiya.
# Dictionary me function store kiya.
# Function ko data "remember" karna sikhaya (Closure).
# Phir bataya ki ye sab kaam Classes/Objects se aur clean tarike se kiya ja sakta hai.


# Dictionary sirf  = Brand Color Speed
# object  = Brand Color Speed Start() Stop() Brake() 
# Dictionary aur Object ka difference samjho.
# Sirf data store karna hi nahi, balki us data ke saath kaam karna bhi seekho.
# Future me Classes aur Objects use kar sako.
# | Dictionary                    | Object                                      |
# | ----------------------------- | ------------------------------------------- |
# | Sirf data store karti hai     | Data + Functions (Methods) dono rakhta hai  |
# | `student["name"]`             | `student.name`                              |
# | Keys aur values               | Attributes aur methods                      |
# | Chhote programs ke liye acchi | Bade aur professional projects ke liye best |


# step 1 -passing a dict  to a fnction
# becky = {
#  "name": "Becy",
#  "age": 34,
#  "eyes": "green"
#  }

# def talk(who, words, why):
#  print(f"I am {who['name']} and {words} and {why}")

# talk(becky, "I am talking here!", "nice")
# two peremeter who and words to usme passing kiya peremeterms



# Step 2 - Talk inside the dict

# def talk(who, words, why):
#     print(f"I am {who['name']} and {words} and {why}")

# becky = {
#     "name": "Becky",
#     "age": 34,
#     "eyes": "green",
#     "talk": talk
# }

# becky["talk"](becky, "I am talking here!", "I like Python.")

# # closures
# def constructor(color, size):
#     print("constructor color",color, "and size", size)

#     def repeater():
#         print("repeater color",color, "and size", size)
    
#     print("exit constuctor")
#     return repeater

# blue_ex = constructor("blue", "xl")
# yello_ex = constructor("Yelloe", "xxl")

# # isme ranch dali utni bar orint hoga ya us range me print hoga
# for i in range(0,3):
#     blue_ex()
#     yello_ex()

# step 4 -a person constructor
def new_person(name, age, eyes):
    person = {
        "name": name,
        "age": age,
        "eyes": eyes
    }
    def talk(words):
        print(f"I am {person['name']} and {words}")
    person["talk"] = talk
    # print(person)
    return person
becky = new_person("Becky", 18, "blue")
becky["talk"]("I am talking here")

# the five simple rules to the game code
#  Rule 1 | Program छोटे-छोटे instructions में बदल जाता है |
# from dis import dis
# dis("""
# x=10
# y=20
# z=x+y
# """)
# LOAD 10
# STORE x
# LOAD 20
# STORE y
# LOAD x
# LOAD y
# ADD
# STORE z
#  Rule 2 | Jump Loop बनाता है
# while True:
#     print("hi")
    # hi print hota jayega anant tak

# | Rule 3 | Condition तय करती है कि Jump होगा या नहीं      |
    # while True:
#     print("hi")
# hi print hota jayega anant tak


# # | Rule 4 | Variables Memory में data रखते हैं             |
# name = "Hitesh"

# | Rule 5 | Input से data आता है और Output से बाहर जाता है |
name = input("Name:")
print(name)



# Input > Store > Test > Jump (अगर जरूरत हो) > Execute > Output
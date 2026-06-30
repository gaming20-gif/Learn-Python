# doing things to dictionaries
# Dictionary Python ka ek data structure hai jo key : value pair me data store karta hai.
# Dictionary aur List me Difference
# List	Dictionary
# Index se access hoti hai	Key se access hoti hai
# fruits[0]	student["name"]

things = ['a', 'b', 'c', 'd']
print(things[1])
things[1] = 'z'
print(things[1])
# value ko chnage ya fir replace kar sakte he add kar sakte our remove bhi kar sakte he
print(things)

stuff = {'name': 'Zed', 'age': 39, 'height': 6 * 12 + 2}
print(stuff['name'])
print(stuff['height'])
# naya add kar sakte
stuff['city'] = "bhuj"
print(stuff)
# isbar remove/delete kiay
stuff.pop('city')
print(stuff)
stuff.pop('height')
print(stuff)

# create a mapping of state to abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}
# create a basic set of states and some cities in them
cities = {
    'CA' : 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}
# add cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print('-' * 10)
print("NY State has: ", cities['NY'])
print("OR State has: ", cities['OR'])

# print some states
print('-' * 10)
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])

# # do it by using the state then cities dict
# print('-' * 10)      #   mi     michigan = detrit   isme state me michigan ki value leg jo = Mi ab vo cities me dehega ki MI he uski value kya he to vo valu he =Detroit to vo print kar dega
print("Michigan has: ", cities[states['Michigan']])
# isme dektta he ki jo cities he wo states me he our he to batata he

# print every state abbreviation
print('-' * 10) 
for state, short_name in list(states.items()):
    print(f"{state} state is abbreviated {short_name}")
# in loop difine two perematers he takes all states info one is state second isshort_name

# this for city
for city, short_name in list(cities.items()):
    print(f"{city} city is abbreviated {short_name}")


# now do both at the same time
print('-' * 10)
for state, short in list(states.items()):
   print(f"{state} state is abbreviated {short}")
   print(f"and has city {cities[short]}")

print('-' * 10)
# safely get a abbreviation by state that might not be there
# state = states.get('New York')ye he state me he
state = states.get('texas')
if not state :
    print("this not state")
# taxas state me nahi he to fir ye print hoga

# get a city with a default value

city = cities.get('TX', 'Does Not Exist')
print(f"The city for the state 'TX' is: {city}")


# .get() method item ko get karta
print(cities)
print(states)
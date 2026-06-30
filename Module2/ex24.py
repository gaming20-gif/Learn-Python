email = {
  "From": "j.smith@example.com",
  "To": "zed.shaw@example.com",
  "Subject": "I HAVE AN AMAZING INVESTMENT FOR YOU!!!"
  };

print(email["From"])

messages = [
 # key: value
 {"to": 'Sun', "from": 'Moon', "message": 'Hi!'},  #0
 {"to": 'Moon', "from": 'Sun', "message": 'What do you want Sun?'}, #1
 {"to": 'Sun', "from": 'Moon', "message": "I'm awake!"},#2
 {"to": 'Moon', "from": 'Sun', "message": 'I can see that Sun.'}#3
 ];

# print(messages[1])
  #  witch   number  add value
print(messages[2]['message'])


languages = [
 {'name': 'Python', 'speed': 'Slow',
 'opinion': ['Terrible', 'Mush']},
 {'name': 'JavaScript', 'speed': 'Moderate',
 'opinion': ['Alright', 'Bizarre']},
 {'name': 'Perl6', 'speed': 'Moderate',
 'opinion': ['Fun', 'Weird']},
 {'name': 'C', 'speed': 'Fast',
 'opinion': ['Annoying', 'Dangerous']},
 {'name': 'Forth', 'speed': 'Fast',
 'opinion': ['Fun', 'Difficult']},
 ];
#       witch   index  key  witch one choose
print(languages[4]['opinion'][1])

fruit = [
    {'kind': 'Apples', 'count': 12, 'rating': 'AAA'},
    {'kind': 'Oranges', 'count': 1, 'rating': 'B'},
    {'kind': 'Pears', 'count': 2, 'rating': 'A'},
    {'kind': 'Grapes', 'count': 14, 'rating': 'UR'}
]
print(fruit[3]['rating'])
cars = [
    {'type': 'Cadillac', 'color': 'Black',
     'size': 'Big', 'miles': 34500},
    {'type': 'Corvette', 'color': 'Red',
     'size': 'Little', 'miles': 1000000},
    {'type': 'Ford', 'color': 'Blue',
     'size': 'Medium', 'miles': 1234},
    {'type': 'BMW', 'color': 'White',
     'size': 'Baby', 'miles': 7890}
]

print(cars[2]['miles'])
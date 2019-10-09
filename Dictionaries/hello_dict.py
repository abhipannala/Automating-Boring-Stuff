# Dictionaries are not ordered so they can't be sliced
import sys

birthdays = {'Alicia': 'Apr 1', 'Bob': 'Jan 15', 'Carol': 'The beginning of all time!'}

while True:
    print("Enter a name: (blank to quit)")
    name = input()
    if name == '':
        sys.exit()  # or break, either work
    elif name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print('The person by the name ' + name + ' does not exist in my database')
        print('What is their birth-date?')
        bDay = input()
        birthdays[name] = bDay
        print('Birthday database updated. Pinging Skynet to implement Doomsday Protocol')

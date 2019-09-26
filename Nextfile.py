## continue statement continues the loop
while True:
    print('Who are you?')
    name=input()
    if name.lower() != 'joe':
        continue
    print('Hello Joe. What is the password? (It is a fish.)')
    password=input()
    if password.lower() == 'swordfish':
        break
print('Access Granted')


## The last flow control concept is sys.exit(). Redo FLOW CONTROL when you have free time. 
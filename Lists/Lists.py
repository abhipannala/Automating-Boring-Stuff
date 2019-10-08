catNames = []

while True:
    print("Enter the name of cat #" + str(len(catNames)+1) + " or enter nothing to stop")
    name = input()
    if name == '':
        break
    else:
        catNames.append(name)

print('The cat names are:')
for a in catNames:
    print(str(catNames.index(a)+1)+') '+a)

"""
Write a function that takes a list value as an argument and returns
a string with all the items separated by a comma and a space, with 'and'
inserted before the last item. For example, passing the previous spam list to
the function would return 'apples, bananas, tofu, and cats'. But your function
should be able to work with any list value passed to it.
"""


def funk(listerino):
    """
    takes a list and returns its contents in string format
    separated by comma, space and an 'and' for the last word
    :param listerino: Your list
    :return:
    """
    f = str()
    for a in listerino:
        if listerino.index(a) == 0:
            f = str(a)
        elif listerino.index(a) != (len(listerino) - 1):
            f = f +', '+ str(a)
        else:
            f = f + ', and ' + str(a)
    return f


def main():
    """
    Takes an input list, and prints it out using funk()
    :return: Nothing
    """
    input_list = []
    i = 1
    print('Please enter your list values or enter nothing to stop')
    while True:
        i += 1
        x = input()
        if x == '':
            break
        else:
            print('Please enter value number {}'.format(i))
            input_list.append(x)
    a = funk(input_list)
    print("The values you've input in the list are {}".format(a))


if __name__ == '__main__':
    main()




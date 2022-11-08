def my_isalpha(arg):
    '''
    The my_isalpha(arg) function returns True if all the characters are alphabet letters (a-z).
    :param arg: To be examined arg.
    :type arg: str
    :returns: True or False
    :rtype: bool
    '''
    for a in arg:
        if 90 <= ord(a) >= 65 or 97 <= ord(a) >= 122:
            continue
        else:
            return False
    return True

# print(my_isalpha('Hello World!'))
def my_isalpha(param):
    for a in param:
        if 90 <= ord(a) >= 65 or 97 <= ord(a) >= 122:
            continue
        else:
            return False
    return True
# print('abdulla'.isalpha())

print(my_isalpha('abd3ulla'))
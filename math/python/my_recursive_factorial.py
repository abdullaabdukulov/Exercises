def my_recursive_factorial(n):
    '''
    This is a recursive function
    to find the factorial of an integer
    '''
    if n==1:
        return 1
    else:
        # recursive call to the function
        return (n* my_recursive_factorial(n-1))
# print(my_recursive_factorial(5))
'''
This problem was asked by Uber.
Given an array of integers, return a new array such that each element at index i of the new
array is the product of all the numbers in the original array except the one at i
Follow-up: what if you can't use division?
'''
import numpy as np
#For my current python version 3.7.8, I'm using numpy.prod()
#Alternatively you can use math.prod() as well, if your python version is 3.8 or above

def using_division(given_array):
    product = np.prod(given_array)
    output = []
    for number in given_array:
        if number == 0:
            updated_array = given_array.copy()
            updated_array.remove(number)
            output.append(np.prod(updated_array))
        else:
            output.append(product//number)
    return output

def not_using_divison(given_array):
    output = []
    for number in given_array:
        updated_array = given_array.copy()
        updated_array.remove(number)
        output.append(np.prod(updated_array))
    return output

if __name__ == "__main__":
    given_array = list(map(int, input().split()))
    print(using_division(given_array))
    print(not_using_divison(given_array))

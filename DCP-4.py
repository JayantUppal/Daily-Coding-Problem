'''
This problem was asked by Stripe.
Given an array of integers, find the first missing positive integer in linear time and constant space.
In other words, find the lowest positive integer that does not exist in the array. The array can
contain duplicates and negative numbers as well.
For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
You can modify the input array in-place.
'''

def segregate(given_arr):
    index = 0
    for i, num in enumerate(given_arr):
        if num <= 0:
            given_arr.insert(index, given_arr.pop(i))
            index += 1
    return given_arr[index:]

def findMissing(pos_arr):
    for num in pos_arr:
        if (abs(num) - 1 < len(pos_arr) and pos_arr[abs(num) - 1] > 0):#0
            pos_arr[abs(num) - 1] = -pos_arr[abs(num) - 1]

    for i, num in enumerate(pos_arr):
        if num > 0:
            return i + 1
    return len(pos_arr) + 1

if __name__ == "__main__":
    given_arr = list(map(int, input().split()))
    print("The smallest positive missing number is ", findMissing(segregate(given_arr)))

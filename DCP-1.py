'''
This problem was recently asked by Google.
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
'''
def output(given_list, k):
    for elem in given_list:
        diff = k - elem
        updated_list = given_list.copy()
        updated_list.remove(elem)
        if diff in updated_list:
            return True
    return False

if __name__ == "__main__":
    given_list = list(map(int, input().split()))
    k = int(input())
    print(output(given_list, k))

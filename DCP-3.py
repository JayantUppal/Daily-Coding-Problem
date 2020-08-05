'''
This problem was asked by Google.
Given the root to a binary tree, implement serialize(root), which serializes the tree into a string,
and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
'''

class Node():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def serialize(root):
    output = {}
    if not root:
        return None

    s_l = serialize(root.left)
    s_r = serialize(root.right)

    #Pre-order traversal
    output['value'] = root.value
    if s_l:
        output['left'] = s_l
    if s_r:
        output['right'] = s_r
    return output

def deserialize(output):
    root = Node(output['value'])
    if output.get('left'):
        root.left = deserialize(output['left'])
    if output.get('right'):
        root.right = deserialize(output['right'])
    return root

if __name__ == "__main__":
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    #For simplicity, serialize(root) will return a dictionary and deserialize(output) will take dictionary as input
    #You can import json to dump and load dictionary to string format
    assert deserialize(serialize(node)).left.left.value == 'left.left', "Test didn't pass"
    print("Test passed!")

'''
Given tree in test case:-
              'root'
              /    \
        'left'      'right'
        /
    'left.left'
'''

class Node:

    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
    def __str__(self):
        return "%d"%(self.data,)


def preOrder(n):
    if n == None:
        return
    preOrder(n.left)
    print n
    preOrder(n.right)

def build_tree(sequence, low, high):
    if low > high:
        return None
    if low == high:
        return Node(sequence[low])
    mid = (low + high)/2
    node = Node(sequence[mid])
    print node
    node.left = build_tree(sequence, low, mid -1)
    node.right = build_tree(sequence, mid + 1, high)
    return node


if __name__ == '__main__':
    n1 = Node(10)
    n2 = Node(8)
    n5 = Node(1)
    n6 = Node(9)
    n3 = Node(16)
    n4 = Node(11)

    n1.left = n2
    n1.right = n3
    n3.left = n4
    n2.left = n5
    n2.right = n6

    #preOrder(n1)


    s = [1,8,9,10,11,16]
    tree = build_tree(s, 0, len(s)-1)
    #preOrder(tree)

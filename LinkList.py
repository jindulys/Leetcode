class Node:
    def __init__(self, data = 0):
        self.data = data
        self.next = None

    def __repr__(self):
        return '%d -> %s'%(self.data, repr(self.next))

    def __str__(self):
        return repr(self)


def deleteNode(head, toDelete):

    if toDelete.next == None:
        return

    tmp = toDelete.next
    toDelete.data = tmp.data
    toDelete.next = tmp.next
    del tmp

def reverseNode(head):
    if head == None or head.next == None:
        return

    pre = None
    nex = None
    while head != None:
        nex = head.next
        #print nex
        head.next = pre
        #print pre
        pre = head
        head = nex
    return pre



if __name__ == '__main__':
    n1 = Node()

    n2 = Node(10)

    n3 = Node(20)

    n2.next = n3
    n1.next = n2

    print n3
    reverseNode(n3)
    print n3

    print n1
    m = reverseNode(n1)
    print m

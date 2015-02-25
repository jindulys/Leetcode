class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.cap = capacity
        self.keyDict = {}
        # head stores the element to remove when the capacity reached
        self.head = None
        # tail stores the recently used element.
        self.tail = None

    # @return an integer
    def get(self, key):

        if key in self.keyDict:
            # move that key node to the list's end
            node = self.keyDict[key]

            self.move_to_tail(node)
            return node.data[1]
        else:
            return -1


    def move_to_tail(self, node):

        if not (node == self.tail):
            if node == self.head:
                self.head = self.head.next
                self.head.pre = None

                self.tail.next = node
                node.pre = self.tail
                self.tail = node
                self.tail.next = None
            else:
                node.pre.next = node.next
                node.next.pre = node.pre

                self.tail.next = node
                node.pre = self.tail
                node.next = None
                self.tail = node

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):

        if len(self.keyDict) >= self.cap:
            self.remove_head_node()

        node = Node()
        node.data = (key, value)
        self.insert_to_tail(node)
        self.keyDict[key] = node

    def remove_head_node(self):

        del self.keyDict[self.head.data[0]]

        if self.head == self.tail:
            self.head = None
            self.pre = None
        else:
            self.head = self.head.next
            self.head.pre = None


10,[set(10,13),set(3,17),set(6,11),set(10,5),set(9,10),get(13),set(2,19),get(2),get(3),set(5,25),get(8),set(9,22),set(5,5),set(1,30),get(11),set(9,12),get(7),get(5),get(8),get(9),set(4,30),set(9,3),get(9),get(10),get(10),set(6,14),set(3,1),get(3),set(10,11),get(8),set(2,14),get(1),get(5),get(4),set(11,4),set(12,24),set(5,18),get(13),set(7,23),get(8),get(12),set(3,27),set(2,12),get(5),set(2,9),set(13,4),set(8,18),set(1,7),get(6),set(9,29),set(8,21),get(5),set(6,30),set(1,12),get(10),set(4,15),set(7,22),set(11,26),set(8,17),set(9,29),get(5),set(3,4),set(11,30),get(12),set(4,29),get(3),get(9),get(6),set(3,4),get(1),get(10),set(3,29),set(10,28),set(1,20),set(11,13),get(3),set(3,12),set(3,8),set(10,9),set(3,26),get(8),get(7),get(5),set(13,17),set(2,27),set(11,15),get(12),set(9,19),set(2,15),set(3,16),get(1),set(12,17),set(9,1),set(6,19),get(4),get(5),get(5),set(8,1),set(11,7),set(5,2),set(9,28),get(1),set(2,2),set(7,4),set(4,22),set(7,24),set(9,26),set(13,28),set(11,26)

    def insert_to_tail(self, node):

        if self.tail is None:
            self.tail = node
            self.head = node
        else:
            node.pre = self.tail
            self.tail.next = node
            self.tail = node


class Node:
    def __init__(self):
        self.pre = None
        self.next = None
        # (key, value)
        self.data = None

    def __eq__(self, other):
        if self.data[0] == other.data[0]:
            return True
        return False

    def __str__(self):
        return str(self.data)

def test():

    cache1 = LRUCache(0)
    print 'Test Non Exist key'
    print "Pass" if cache1.get(56) == -1 else "Wrong get no exist key"


    print 'Test Delete least Recent key'
    cache2 = LRUCache(1)

    cache2.set(2, "The first key")
    print cache2.get(2)
    cache2.set(3, "The second key")
    print cache2.get(3)
    print cache2.get(3)




if __name__ == '__main__':

    test()

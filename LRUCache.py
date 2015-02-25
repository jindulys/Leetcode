class ListNode:
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, node):
        if self.head is None:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail
        self.tail = node

    def delete(self, node):
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next
        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev
        del node

class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.list = LinkedList()
        self.dict = {}
        self.capacity = capacity

    def _insert(self, key, val):
        node = ListNode(key, val)
        self.list.insert(node)
        self.dict[key] = node


    # @return an integer
    def get(self, key):
        if key in self.dict:
            val = self.dict[key].val
            self.list.delete(self.dict[key])
            self._insert(key, val)
            return val
        return -1


    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, val):
        if key in self.dict:
            self.list.delete(self.dict[key])
        elif len(self.dict) == self.capacity:
            del self.dict[self.list.head.key]
            self.list.delete(self.list.head)
        self._insert(key, val)




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

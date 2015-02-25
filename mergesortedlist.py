# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        if l1 == None:
            return l2
        elif l2 == None:
            return l1
        else:
            dummy = ListNode()
            p = dummy
            while l1 != None and l2 != None:
                tmp = None
                if l1.val < l2.val:
                    tmp = l1
                    l1 = l1.next
                    tmp.next = None
                else:
                    tmp = l2
                    l2 = l2.next
                    tmp.next = None
                p.next = tmp
                p = p.next

            if l1 == None:
                p.next = l2
            else:
                p.next = l1
            return dummy.next

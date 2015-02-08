# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def sortList(self, head):

        if head == None or head.next == None:
            return head

        fast = head
        slow = head

        while fast.next != None and fast.next.next != None:
            fast = fast.next.next
            slow = slow.next

        fast = slow.next
        slow.next = None

        slow = head
        slow = self.sortList(slow)
        fast = self.sortList(fast)

        result = self.mergeList(slow, fast)
        return result

    def mergeList(self,node1, node2):

        dummy = ListNode(0)
        if node1 == None:
            return node2
        elif node2 == None:
            return node1

        tmp = dummy
        while node1 != None and node2 != None:
            if node1.val > node2.val:
                tmp.next = node2
                node2 = node2.next
            else:
                tmp.next = node1
                node1 = node1.next
            tmp = tmp.next

        if node1 == None:
            tmp.next = node2
        else:
            tmp.next = node1
        return dummy.next

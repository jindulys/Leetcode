# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return nothing
    def reorderList(self, head):

        if head == None or head.next == None or head.next.next == None:
            return
        dump = ListNode(0)
        dump.next = head

        dump2 = self.diffRun(head)

        toR = dump2.next
        dump2.next = None

        reversed = self.reverse(toR)

        tmp = head

        while reversed:
            tmp1 = tmp.next
            tmp2 = reversed.next
            tmp.next = reversed
            reversed.next = tmp1
            tmp = tmp1
            reversed = tmp2


    def reverse(self, head):
        dummy = ListNode(0)
        dummy.next = None

        while head != None:
            tmp = head.next
            head.next = dummy.next
            dummy.next = head
            head = tmp
        return dummy.next

    def diffRun(self, head):
        p1 = head
        p2 = head

        while p2 and p2.next:
            p2 = p2.next.next
            p1 = p1.next
        return p1
        

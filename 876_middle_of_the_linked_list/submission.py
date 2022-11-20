# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # linked lists are not iterable (i.e. python lists (arrays))
        # return head[int(len(list(head))/2):]
        count = 0
        print dir(head)
        working_head = head
        while working_head.next:
            count += 1
            working_head = working_head.next
        count += 1
        to_next = int(count/2)
        for n in range(to_next):
            head = head.next
        return head
        

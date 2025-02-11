# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        if not list1:
            return list2
        if not list2:
            return list1
        result = None
        head = None
        current1 = list1
        current2 = list2
        while current1 and current2:
            if result:
                result.next = ListNode()
                result = result.next
            else:
                result = ListNode()
                head = result
            if current1.val < current2.val:
                result.val = current1.val
                current1 = current1.next
            else:
                result.val = current2.val
                current2 = current2.next
        if current1:
            result.next = current1
        else:
            result.next = current2
        return head

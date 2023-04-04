# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = fast = head
        # fast : point to n-th from beginning
        for _ in range(n):
            fast = fast.next
        if not fast:
            return head.next
        # for reverse, progress pointer until end - for both fast and slow
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next

        return head

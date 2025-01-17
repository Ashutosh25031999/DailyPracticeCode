class Solution:
    def reverseBetween(self, head, left, right):
        if not head or not head.next or left == right:
            return head
        temp = ListNode(val=-1e9)
        temp.next = head
        curr = temp
        for _ in range(left - 1):
            curr = curr.next

        temp_curr = curr.next
        for _ in range(right - left):
            nxt = temp_curr.next
            temp_curr.next = nxt.next
            nxt.next = curr.next
            curr.next = nxt

        return temp.next

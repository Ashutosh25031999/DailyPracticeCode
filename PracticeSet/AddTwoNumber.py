# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        dummyHead = ListNode(0)
        tail = dummyHead
        carry = 0

        while l1 is not None or l2 is not None or carry != 0:
            digi1 = l1.val if l1 is not None else 0
            digi2 = l2.val if l2 is not None else 0

            sum = digi1 + digi2 + carry
            digit = sum % 10
            carry = sum // 10

            newNode = ListNode(digit)
            tail.next = newNode
            tail = tail.next

            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None 

        result = dummyHead.next
        dummyHead.next = None

        return result

# Helper function to create a linked list from a list of values
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to print linked list values
def print_linked_list(node):
    values = []
    while node:
        values.append(node.val)
        node = node.next
    print(values)

# Example test cases
l1 = create_linked_list([2, 4, 3])  # Represents the number 342
l2 = create_linked_list([5, 6, 4])  # Represents the number 465

solution = Solution()
result = solution.addTwoNumbers(l1, l2)
print_linked_list(result)  # Output should be [7, 0, 8], representing the number 807

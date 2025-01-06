class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        cur = dummy = ListNode()
        while list1 and list2:               
            if list1.val < list2.val:
                cur.next = list1
                list1, cur = list1.next, list1
            else:
                cur.next = list2
                list2, cur = list2.next, list2
                
        if list1 or list2:
            cur.next = list1 if list1 else list2
            
        return dummy.next

# Helper function to create linked list from list
def create_linked_list(elements):
    dummy = ListNode()
    cur = dummy
    for e in elements:
        cur.next = ListNode(e)
        cur = cur.next
    return dummy.next

# Helper function to print linked list
def print_linked_list(head):
    elements = []
    while head:
        elements.append(head.val)
        head = head.next
    print(elements)

# Test cases
list1 = create_linked_list([1, 2, 4])
list2 = create_linked_list([1, 3, 4])

solution = Solution()
merged_list = solution.mergeTwoLists(list1, list2)
print_linked_list(merged_list)  # Output: [1, 1, 2, 3, 4, 4]

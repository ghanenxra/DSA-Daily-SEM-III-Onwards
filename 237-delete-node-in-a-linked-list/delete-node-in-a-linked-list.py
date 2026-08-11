# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next





        # prev = ListNode()
        # next_of_prev = ListNode(0)
        # while prev.next == node:
        #     prev.next.next = node.next
        #     return




        # # if self.head == None:
        # #     return
        # if node == None:
        #     pass
        # else:
        #     temp=self.head

        #     while temp.next:
        #         temp.temp.next
        #         if temp.next.val == val:
        #             temp.next = temp.next.next
        #             return
                
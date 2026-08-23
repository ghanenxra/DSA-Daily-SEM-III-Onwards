
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = 0
        place = 1
        while l1:
            num1 += l1.val * place
            place *= 10 
            l1 = l1.next
        num2 = 0
        place1 = 1
        while l2:
            num2 += l2.val * place1
            place1 *= 10
            l2 = l2.next
        
        total_sum = num1 + num2

        if total_sum == 0:
            return ListNode(0)

        #Create a new dummy linklist 
        dummy = ListNode(0)
        curr = dummy
        while total_sum>0:
            curr.next = ListNode(total_sum%10)
            curr = curr.next
            total_sum //= 10

        return dummy.next
        

            
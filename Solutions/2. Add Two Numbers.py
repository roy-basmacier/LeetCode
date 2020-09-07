# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = []
        i = 0
        overload = False
        while l1 != None or l2 != None:
            if overload:
                res.append(1)
            else:
                res.append(0)
            overload = False  
            if l1 != None and l2 != None:
                if (res[i] + l1.val + l2.val) > 9:
                    overload = True
                res[i] = (res[i] + l1.val + l2.val) % 10

                l1 = l1.next
                l2 = l2.next
                
            elif l1 != None and l2 == None:
                if (res[i] + l1.val) > 9:
                    overload = True
                res[i] = (res[i] + l1.val) % 10

                l1 = l1.next
                
            elif l2 != None and l1 == None:
                if (res[i] + l2.val) > 9:
                    overload = True
                res[i] = (res[i] + l2.val) % 10
                l2 = l2.next
            print(res)
            i += 1
            
            
        if overload:
            res.append(1)
        return res         
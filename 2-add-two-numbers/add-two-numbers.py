# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
         
        list1=[]
        list2=[]
        
        while l1:
            list1.append(l1.val)
            l1=l1.next

        while l2:
            list2.append(l2.val)
            l2=l2.next    




        b=map(str , list1)

        i=map(str , list2)
        v=int("".join(b[::-1]))
        k=int("".join(i[::-1]))
        total=(v+k)
        t=str(total)[::-1]

        q=[]
        for r in t:
            c=int(r)
            q.append(c)
            
            
        d=ListNode()
        f=d

        for num in q:
            f.next=ListNode(num)
            f=f.next

        return d.next    

        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        
        if not list1:
            return list2
        elif not list2:
            return list1
        
        
        prev = ListNode()
        head = None        
        
        while list1 and list2:
            
            if list1.val < list2.val:
                
                if head == None:
                    
                    prev = list1
                    head = prev
                    
                else:
                    prev.next = list1
                    prev = prev.next
                                      
                list1 = list1.next

            else:
                
                if head == None:
                    
                    prev = list2
                    head = prev
                    
                else:
                    prev.next = list2
                    prev = prev.next
                    
                list2 = list2.next
            
                
                
        if list1:
            prev.next = list1
        elif list2:
            prev.next = list2
        
        
        return head
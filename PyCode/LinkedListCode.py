import sys

class LinkedListCode:
    
    

    class ListNode:
        def __init__(self, x):
            self.val = x
            self.next = None

    def __init__(self):
        pass
    
    '''Linked List Cycle'''
    def hasCycle(self, head):
        if not head or not head.next:
            return False  
        fast = slow = head
        while slow.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
    
    '''Linked List Cycle II'''
    def detectCycle(self, head):
        if not head or not head.next:
            return None
        slow = fast = head
        head2 = None
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return fast
        return None
    
    '''Intersection of Two Linked Lists'''
    def getIntersectionNode(self, headA, headB):
        p1 = headA
        p2 = headB
        while p1 != p2:
            p1 = p1.next if p1 else headB
            p2 = p2.next if p2 else headA
        return p1

    '''Remove Duplicates from Sorted List'''  
    def deleteDuplicates(self, head):
        if not head or not head.next:
            return head
        last = head
        p = head.next
        while p:
            if last.val != p.val:
                last = p
            else:
                last.next = p.next
            p = p.next
        return head
    
    '''Remove Duplicates from Sorted List II'''
    def deleteDuplicates2(self, head):
        if not head or not head.next:
            return head
        p1 = head
        cur = None
        result = None
        last = None
        while p1:
            if (not p1.next or p1.val != p1.next.val) and (not last or p1.val != last.val):
                if cur:
                    cur.next = p1
                    cur = p1
                else:
                    result = p1
                    cur = p1
            last = p1
            p1 = p1.next
        if cur:
            cur.next = None
        return result
    
    '''Merge Two Sorted Lists'''
    def mergeTwoLists(self, l1, l2):
        p1 = l1
        p2 = l2
        cur = result = None
        while p1 or p2:
            if not p1 or (p2 and p2.val <= p1.val):
                if not result:
                    cur = p2
                    result = cur
                else:
                    cur.next = p2
                    cur = cur.next
                p2 = p2.next
            else:
                if not result:
                    cur = p1
                    result = cur
                else:
                    cur.next = p1
                    cur = cur.next
                p1 = p1.next
        return result

    '''Merge k Sorted Lists'''
    def mergeKLists(self, lists):
        if len(lists) < 1:
            return None
        temp = lists[:]
        while len(temp) != 1:
            next = temp[:]
            for i in range(0, len(temp), 2):
                if i+1 > len(temp) - 1:
                    continue
                newList = self.mergeTwoLists(temp[i], temp[i+1])
                next.remove(temp[i])
                next.remove(temp[i+1])
                next.append(newList)
            temp = next            
        return temp[0]  

    '''Reverse Linked List'''
    def reverseList(self, head):
        pre = None
        while head:
            temp = head
            head = head.next
            temp.next = pre
            pre = temp
        return pre
    
    '''Reverse Linked List II'''
    def reverseBetween(self, head, m, n):
        i = 1
        cur = head
        preStart = None
        start = None
        result = head
        pre = None
        while cur:
            if i < m:
                if i == m - 1:
                    preStart = cur
                cur = cur.next 
            elif i > n:
                start.next = cur
                break
            else:
                if i == n and preStart:
                    preStart.next = cur
                temp = cur
                cur = temp.next
                temp.next = pre
                if start == None:
                    start = temp
                pre = temp 
            i += 1  
        return head if m > 1 else pre

    '''Swap Nodes in Pairs'''
    def swapPairs(self, head):
        if not head or not head.next:
            return head
        i = 0
        pre = None
        cur = head
        result = None
        preStart = None
        while cur:
            if i % 2 == 1:
                temp = cur
                cur = temp.next
                pre.next = temp.next
                temp.next = pre
                if preStart:
                    preStart.next = temp
                preStart = pre
                if not result:
                    result = temp
            else:
                pre = cur
                cur = cur.next
            i += 1
        return result if result else head
            
    'Sort List'
    def sortList(self, head):
        if not head or not head.next:
            return head
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next
        middle = slow.next
        slow.next = None
        return self.mergeTwoLists(self.sortList(head), self.sortList(middle))
    
    ''' Rotate List'''
    def rotateRight(self, head, k):
        if k == 0 or not head:
            return head
        cur = head
        total = 0
        result = None
        while cur:
            cur = cur.next
            total += 1
        k = k % total
        if k == 0:
            return head
        cur = head
        i = 1
        while cur:
            if total - i == k:
                temp = cur
                cur = cur.next
                result = cur
                temp.next = None
            elif i == total:
                cur.next = head
                break
            else:
                cur = cur.next
            i += 1
        return result
    
    '''Reorder List'''
    def reorderList(self, head):
        if not head:
            return 
        fast = slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        if fast == head:
            return 
        middle = slow
        backList = middle.next
        middle = slow.next
        slow.next = None

        cur = middle
        pre = None
        while cur:
            temp = cur
            cur = cur.next
            temp.next = pre
            pre = temp
        middle = pre
        cur1 = head
        cur2 = middle 
        while cur1 and cur2:
            temp1 = cur1
            temp2 = cur2
            cur1 = cur1.next
            cur2 = cur2.next
            temp1.next = temp2
            temp2.next = cur1
        return 

    '''Partition List'''
    def partition(self, head, x):
        if not head or not head.next:
            return head
        small = smallHead = None
        big = bigHead = None
        cur = head
        while cur:
            temp = cur
            cur = cur.next
            if temp.val < x:
                if smallHead:
                    small.next = temp
                    small = temp
                else:
                    small = smallHead = temp
            else:
                if bigHead:
                    big.next = temp
                    big = temp
                else:
                    big = bigHead = temp
            temp.next = None
        if not smallHead:
            return bigHead
        else:
            small.next = bigHead
            return smallHead
    
    '''Add Two Numbers'''
    def addTwoNumbers(self, l1, l2):
        cur1 = l1
        cur2 = l2
        cur = head = None
        carry = 0
        while cur1 or cur2:
            value = 0
            if cur1 and cur2:
                value = cur1.val + cur2.val
                cur1 = cur1.next
                cur2 = cur2.next
            elif not cur1:
                value = cur2.val
                cur2 = cur2.next
            else:
                value = cur1.val
                cur1 = cur1.next
            value += carry
            remain = value % 10
            carry = value / 10
            if not cur:
                head = cur = ListNode(remain)
            else:
                cur.next = ListNode(remain)
                cur = cur.next
        if carry == 1:
            cur.next = ListNode(1)
        return head
    

    class RandomListNode:
        def __init__(self, x):
            self.label = x
            self.next = None
            self.random = None

    '''Copy List with Random Pointer'''
    def copyRandomList(self, head):
        cur = head
        rCur = result = None
        mapping = {}

        cur = head
        while cur:
            temp = cur
            cur = cur.next
            mapping[temp] = rCur
            
        while cur:
            temp = cur
            cur = cur.next
            if not result:
                rCur = result = RandomListNode(temp.label)
                if temp.random:
                    mapping[temp] = rCur
            else :
                rCur.next = RandomListNode(temp.label)
                if temp.random:
                    mapping[temp] = rCur
                rCur = rCur.next

       
            
        


        




        
        


            

            
                    
                
                
                    
        

        
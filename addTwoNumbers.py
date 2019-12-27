import unittest
class ListNode:
    def __init__(self,initVal):
        self.val = initVal
        self.next = None

    def equals(self,comp):
        currComp = comp
        currObj = self
        while True:
            if (currObj.next == None) != (currComp.next ==None):
                return False
            elif (currObj.val != currComp.val):
                return False
            elif (currObj.next == None and currComp.next ==None):
                return True
            else:
                currObj = currObj.next
                currComp = currComp.next
            

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        Takes 2 linked lists representing nonegative integers: 345: 5->4->3->.
        and outputs them added together
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        currVal =l1.val+l2.val
        if currVal>9:
            currVal-=10
            over=True
        else:
            over=False
        result = ListNode(currVal)
        currN1 = l1
        currN2 = l2
        currRes = result;
        while True:
            if (currN1.next != None and currN2.next != None):
                currN1 = currN1.next
                currN2 = currN2.next
                currVal = currN1.val+currN2.val
            elif (currN1.next !=None):
                currN1 = currN1.next
                currVal = currN1.val
            elif (currN2.next !=None):
                currN2 = currN2.next
                currVal = currN2.val
            else:
                if over:
                    currRes.next = ListNode(1)
                return result
            if over:
                currVal+=1
                over = False
            if currVal >9:
                currVal-=10
                over = True
            currRes.next = ListNode(currVal)
            currRes = currRes.next
                         
class add2NumsTestCase(unittest.TestCase):

    def testBasicAddSum(self):
        addTwoNumbers = Solution().addTwoNumbers
        # Test 2+5=7
        l1=ListNode(2)
        l2=ListNode(5)
        exp = ListNode(7)
        self.assertTrue(addTwoNumbers(l1,l2).equals(exp))
        self.assertTrue(addTwoNumbers(l2,l1).equals(exp))
        #Test 42+5=47
        l1.next = ListNode(4)
        exp.next = ListNode(4)
        self.assertTrue(addTwoNumbers(l1,l2).equals(exp))
        #Test 42+65=107
        l2.next = ListNode(6)
        exp.next.val = 0
        exp.next.next = ListNode(1)
        self.assertTrue(addTwoNumbers(l1,l2).equals(exp))
        #Test 42+465=507
        l2.next.next=ListNode(4)
        exp.next.next.val=5
        self.assertTrue(addTwoNumbers(l1,l2).equals(exp))
        #Test 342+465=807
        l1.next.next=ListNode(3)
        exp.next.next.val=8
        self.assertTrue(addTwoNumbers(l1,l2).equals(exp))
        #Test 99+1=100
        l1 = ListNode(9)
        l1.next = ListNode(9)
        l2 = ListNode(1)
        exp = ListNode(0)
        exp.next = ListNode(0)
        exp.next.next = ListNode(1)
        self.assertTrue(addTwoNumbers(l1,l2).equals(exp))
        
        
if __name__ == '__main__':
    unittest.main()

import unittest

class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        if k<1:
            raise ValueError("Must Input Positive input")
        self.size=k
        self.tail=-1        
        self.head=-1
        self.circQue=[None]*self.size
        
        

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        elif self.isEmpty():
            self.head=0
        self.tail = (self.tail+1) % self.size
        self.circQue[self.tail] = value
        return True
        

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        elif self.head==self.tail:
            self.head=-1
            self.tail=-1
            return True
        self.head = (self.head+1) % self.size 
        return True
        
        
    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.isEmpty():
            return -1
        else:
            return self.circQue[self.head]

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self.isEmpty():
            return -1
        else:
            return self.circQue[self.tail]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.head==-1        

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return ((self.tail+1)%self.size) == self.head

        
class circularQueueTest(unittest.TestCase):

    def testEmptyCircQue(self):
        myQue = MyCircularQueue(2)
        self.assertTrue(myQue.isEmpty())
        self.assertTrue(myQue.enQueue(1))
        self.assertFalse(myQue.isEmpty())
        self.assertTrue(myQue.deQueue())
        self.assertTrue(myQue.isEmpty())
        
    def testFrontCircQue(self):
        myQue = MyCircularQueue(2)
        self.assertEqual(myQue.Front(),-1)
        self.assertTrue(myQue.enQueue(2))
        self.assertEqual(myQue.Front(),2)
        self.assertTrue(myQue.enQueue(4))
        self.assertEqual(myQue.Front(),2)

        
    def testRearCircQue(self):
        myQue = MyCircularQueue(2)
        self.assertEqual(myQue.Front(),-1)
        myQue.enQueue(2)
        self.assertEqual(myQue.Rear(),2)
        myQue.enQueue(4)
        self.assertEqual(myQue.Rear(),4)

    def testEnDeQueueCircQue(self):
        myQue = MyCircularQueue(3)
        self.assertTrue(myQue.enQueue(0))
        self.assertTrue(myQue.enQueue(1))
        self.assertTrue(myQue.enQueue(2))
        self.assertEqual(myQue.Front(),0)
        self.assertEqual(myQue.Rear(),2)
        self.assertFalse(myQue.enQueue(3))
        self.assertTrue(myQue.deQueue())
        self.assertTrue(myQue.enQueue(3))
        self.assertEqual(myQue.Front(),1)
        self.assertEqual(myQue.Rear(),3)

    def testGivenTestCase(self):
        myQue = MyCircularQueue(6)
        self.assertTrue(myQue.enQueue(6))
        self.assertEqual(myQue.Rear(),6)
        self.assertEqual(myQue.Rear(),6)
        self.assertTrue(myQue.deQueue())
        self.assertTrue(myQue.enQueue(5))
        self.assertEqual(myQue.Rear(),5)
        self.assertTrue(myQue.deQueue())
        self.assertEqual(myQue.Front(),-1)
        self.assertFalse(myQue.deQueue())
        self.assertFalse(myQue.deQueue())
        self.assertFalse(myQue.deQueue())

if __name__ == '__main__':
    unittest.main()



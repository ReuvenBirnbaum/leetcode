import unittest
from typing import List

class twoSumSolution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        size=len(nums)
        stop=False 
        for fir in range(size-1):
            firNum = nums[fir]
            for sec in range(fir+1,size):
                if (firNum+nums[sec])==target:
                    stop=True
                    break
            if stop:
                break
        if (not stop):
            return [-1]
        return [fir, sec]

class twoSumTestCase(unittest.TestCase):

    def testBasicTwoSums(self):
        twoSums = twoSumSolution().twoSum
        self.assertEqual(twoSums([1,2,3],3),[0,1])
        self.assertEqual(twoSums([1,2,3],4),[0,2])
        self.assertEqual(twoSums([1,2,3],5),[1,2])
        self.assertEqual(twoSums([3,2,4],6),[1,2])

    def testFalseTwoSums(self):
        twoSums = twoSumSolution().twoSum       
        self.assertEqual(twoSums([1,2,3],0),[-1])

if __name__ == '__main__':
    unittest.main()

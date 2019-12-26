import unittest
from typing import List

class twoSumSolution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        index=0;
        complament = dict()
        size=len(nums)

        while index<size:
            #Check if each element is not in a complament dictionary:
            # if not found ; put the elemnt in dictionary
            # otherwise return list with complament and current index 
            if target-nums[index] not in complament:
                complament[nums[index]] = index
                index+=1
            else:
                return [complament[target-nums[index]],index]
    

    

class twoSumTestCase(unittest.TestCase):

    def testBasicTwoSums(self):
        twoSums = twoSumSolution().twoSum
        self.assertEqual(twoSums([1,2,3],3),[0,1])
        self.assertEqual(twoSums([1,2,3],4),[0,2])
        self.assertEqual(twoSums([1,2,3],5),[1,2])
        self.assertEqual(twoSums([3,2,4],6),[1,2])
        self.assertEqual(twoSums([2,7,11,15],9),[0,1])
                
if __name__ == '__main__':
    unittest.main()

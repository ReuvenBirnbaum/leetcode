import unittest

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        size =len(s)
        if size <1:
            return 0
        result = 1
        for init in range(size-1):
            if (size-init<=result):
                break
            found = [s[init]]
            for fin in range(init+1,size):
                if s[fin] not in found:
                    found.append(s[fin])
                else:
                    break
            if len(found)>result:
                result = len(found)
        return result

class lengthTestCase(unittest.TestCase):

    def testBasiclength(self):
        lLSS = Solution().lengthOfLongestSubstring
        self.assertEqual(lLSS("bbbbb"),1)
        self.assertEqual(lLSS("pwwkew"),3)
        self.assertEqual(lLSS("abcabcbb"),3)
        
                
if __name__ == '__main__':
    unittest.main()

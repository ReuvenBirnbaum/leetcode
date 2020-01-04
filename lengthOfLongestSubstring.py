import unittest

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        size =len(s)
        i,j,ans= 0,0,0
        found = dict()
        while j<size:
            if (s[j] not in found):
              found[s[j]] =j
              j+=1
              ans = max(j-i,ans)
            else:
                found.pop(s[i])
                i+=1
                if size-i<ans:
                    break
        return ans
            

        
class lengthTestCase(unittest.TestCase):

    def testBasiclength(self):
        lLSS = Solution().lengthOfLongestSubstring
        self.assertEqual(lLSS("bbbbb"),1)
        self.assertEqual(lLSS("pwwkew"),3)
        self.assertEqual(lLSS("abcabcbb"),3)
        
                
if __name__ == '__main__':
    unittest.main()

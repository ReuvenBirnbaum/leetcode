import unittest

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Finds the length of the longest substring of the given string without 
        repeating characters
        :type s: str
        :rtype int
        """
        size =len(s)
        i,j,ans= 0,0,0
        found = dict()
        # Iterate through array with a window defined by [i,j)  
        while j<size:
            # If j^th character not found redefine max if neccesary 
            if (s[j] not in found):
                ans = max(j-i+1,ans)
            # Move i^th index to the next found character while intermediate
            # found elements
            else:
                iNew = found[s[j]]+1
                while i<iNew:
                    found.pop(s[i])
                    i+=1
                if size-i<ans:
                    break
            # Insert the found character and inrement j
            found[s[j]]=j
            j+=1
        return ans
            

        
class lengthTestCase(unittest.TestCase):

    def testBasiclength(self):
        lLSS = Solution().lengthOfLongestSubstring
        self.assertEqual(lLSS("wobgrovw"),6)
        self.assertEqual(lLSS("bbbbb"),1)
        self.assertEqual(lLSS("pwwkew"),3)
        self.assertEqual(lLSS("abcabcbb"),3)
        self.assertEqual(lLSS("tmmzuxt"),5)
        

                
if __name__ == '__main__':
    unittest.main()

# https://leetcode.com/problems/reverse-vowels-of-a-string/description/

# Given a string s, reverse only all the vowels in the string and return it.
# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        reverse = deque(list())
        original = []
        for i in s:
            if i in vowels:
                reverse.appendleft(i)
                original.append(0)
            else:
                original.append(i)
        ans = str()
        for i in original:
            if i == 0:
                ans = ans + reverse.popleft()
            else:
                ans = ans + i
        return ans


# by other people
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels=[i for i in s if i in "aeiouAEIOU"]
        result=[i if i not in "aeiouAEIOU" else vowels.pop() for i in s]
        return "".join(result)
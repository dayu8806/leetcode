# 目的：判斷一個字串是否為回文
import re
def is_palindrome(s: str) -> bool:

    filtered = re.sub(r'[^A-Za-z0-9]', '', s).lower()
    # r'[^A-Za-z0-9]' ^：否定字元集（即「不是...的東西」）而 A-Za-z0-9：英文字母（大小寫）+ 數字。所以這表示：「不是英文字母或數字的東西」
    # re.sub(pattern, replacement, string): 找出所有不合法的字元（非字母數字）=> 把它們通通換成空字串 '' => .lower() 把全部轉成小寫（忽略大小寫）

    return filtered == filtered[::-1]  # filtered[::-1] 是反轉字串的語法

#不用re寫
def is_palindrome(s: str) -> bool:
    filtered = ''.join(c.lower() for c in s if c.isalnum())  # c.isalnum() → 判斷是否為英數字（相當於正則裡的 [A-Za-z0-9]）
    return filtered == filtered[::-1]

print(is_palindrome("A man, a plan, a canal: Panama"))  # 輸出: True
# 總結：
# re.sub()   	清除不必要符號，只保留字母數字
# str.lower()	忽略大小寫
# s[::-1]	    字串反轉


# 計算兩個正整數的最大公因數（GCD）：使用用歐幾里得算法
def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return abs(a)

print(gcd(54, 24))  # 輸出: 6


# 給定兩個已排序的整數串列，請將它們合併為一個排序串列。
def merge_sorted(list1, list2):
    i = j = 0
    merged = []
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            merged.append(list1[i]); i += 1
        else:
            merged.append(list2[j]); j += 1
    # 接續剩餘元素
    merged.extend(list1[i:]); merged.extend(list2[j:])
    return merged

print(merge_sorted([1,3,5], [2,4,6,8]))
# 輸出: [1, 2, 3, 4, 5, 6, 8]


# 給定只包含 ()[]{} 的字串，判斷括號是否有效匹配。例如 "()[]{}" 為有效，但 "([)]" 無效。
def is_valid_parentheses(s: str) -> bool:
    stack = []
    mapping = {')': '(', ']': '[', '}': '{'}
    for ch in s:
        if ch in mapping:  # 是右括號
            if not stack or stack[-1] != mapping[ch]:
                return False
            stack.pop()
        else:
            stack.append(ch)  # 左括號壓入堆疊
    return not stack

print(is_valid_parentheses("()[]{}"), is_valid_parentheses("([)]"))
# 輸出: True False


# 給定整數陣列，找出連續子陣列之最大和。例如 [-2,1,-3,4,-1,2,1,-5,4] 的最大和為 6（子陣列 [4,-1,2,1]）。
# 使用 Kadane’s Algorithm 線性求解：
def max_subarray(nums):
    max_so_far = nums[0]
    current_sum = 0
    for num in nums:
        current_sum = max(num, current_sum + num)  # 現在的最大總和，如果現在的值比目前的總和大，則捨去之前加總的值
        max_so_far = max(max_so_far, current_sum)  # 判斷目前的最大值是否比目前最大的大
    return max_so_far

print(max_subarray([-2,1,-3,4,-1,2,1,-5,4]))  # 輸出: 6
"""
双指针法：左右指针，满足条件右移；不满足条件左移

a       b      c      a      b      c      b      b
(0,0)  (0,1)  (0,2)  (0,3)  (0,4)  (0,5)  (0,6)  (0,7)
       (1,1)  (1,2)  (1,3)  (1,4)  (1,5)  (1,6)  (1,7)
              (2,2)  (2,3)  (2,4)  (2,5)  (2,6)  (2,7)
                     (3,3)  (3,4)  (3,5)  (3,6)  (3,7)
                            (4,4)  (4,5)  (4,6)  (4,7)
                                   (5,5)  (5,6)  (5,7)
                                          (6,6)  (6,7)
                                                 (7,7)

假设(left, right)两个指针；
1. 满足条件 => 右移 right
2. 不满足条件 => 左移 left
注意: (x, x) 相同的情况下一定是满足条件的

其中 "abc" 满足条件的时候，(1, 1) (1, 2)和 (2, 2) 也是满足条件的，可以跳过；
"abca" 不满足条件的时候 "abcab" 也不满足条件，可以跳过，同理直到末位都不满足，都可以跳过；

"""

def lengthOfLongestSubstring(strs: str) -> int:
    left, max_len = 0, 0
    char_set = set()

    for right, s in enumerate(strs):
        # 满足条件 => 右移
        while s in char_set:
            char_set.remove(strs[left])
            left += 1

        char_set.add(s)
        max_len = max(max_len, right - left + 1)

    return max_len

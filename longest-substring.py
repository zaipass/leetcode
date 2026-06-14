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

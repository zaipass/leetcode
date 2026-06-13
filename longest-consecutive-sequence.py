from typing import List

# AI coding
def longestConsecutive(nums: List[int]) -> int:
    if not nums:
        return 0

    num_set = set(nums)
    longest = 0

    for num in num_set:
        # 只从连续序列的起点开始扩展，避免重复计算。
        if num - 1 in num_set:
            continue

        current = num
        length = 1

        while current + 1 in num_set:
            current += 1
            length += 1

        longest = max(longest, length)

    return longest


aa = longestConsecutive([])
print(aa)

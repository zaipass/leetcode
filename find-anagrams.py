import collections


"""
优化版本：窗口滑动
分析：
目标字符串是固定的长度
按照字符串的长度每次+1后移对比，那么每次改变的其实只有最后一个字符
=> 只需要修改最左侧和新的字符就行，不需要每次对比固定长的字符
"""
def findAnagramsFast(s, p):
    if len(p) > len(s):
        return []

    need = collections.defaultdict(int)
    window = collections.defaultdict(int)
    result = []

    for ch in p:
        need[ch] += 1

    window_size = len(p)

    for i, ch in enumerate(s):
        window[ch] += 1

        if i >= window_size:
            left_char = s[i - window_size]
            window[left_char] -= 1
            if window[left_char] == 0:
                del window[left_char]

        if window == need:
            result.append(i - window_size + 1)

    return result


# 复杂度高
def findAnagrams(strs, query_str):
    query_map = collections.defaultdict(int)
    aim_map = collections.defaultdict(int)
    result = []

    for c in query_str:
        query_map[c] += 1

    length = len(query_str)
    for left, _ in enumerate(strs):
        right = left + length
        if right >= len(strs):
            break

        aim_map.pop(strs[left - 1], None)
        aim_map[strs[right]] = aim_map.get(strs[right], 0) + 1

        if aim_map == query_map:
            result.append(left)
    return result


r = findAnagrams("cbaebabacd", "abc")
print(r)

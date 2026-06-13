import collections
from typing import List

# 字母异位词分组
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result_map = collections.defaultdict(list)

        for data in strs:
            key = ''.join(sorted(data))
            result_map[key].append(data)

        return list(result_map.values())
    
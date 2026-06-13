# 两数之和
# 1. 双 for 循环
# 2. map 存储已经访问过的数字，查询目标值是否存在 => key: 值； value: 索引
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        _map = {}
        for index, num in enumerate(nums):
            # 查询的目标值
            target_num = target - num
            res = _map.get(target_num)
            # 当前的值存不存在都要塞进map
            _map[num] = index
            if res is not None:
                return sorted([index, res])
        return []

# 列表中三个数字和为0
# 夹逼法； 双指针法
# for 最外层找 老大 => 0 - 老大 = 双指针
# 双指针求和
# ！！！重复的数字跳过
# 注意：1. set 消耗内存； 2. item in list 消耗时间
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # 抖音解说解答出来的 https://www.douyin.com/user/self/search/Sum%E4%B8%89%E6%95%B0%E4%B9%8B%E5%92%8C?aid=5eaff5eb-797e-42f7-a7cd-01add56208b7&modal_id=7616286839879601462&type=general
        nums.sort()
        res = []

        for i, num in enumerate(nums):
            if num == nums[i - 1] and i > 0:
                continue

            find_num = 0 - num
            left, right = i + 1, len(nums) - 1
            while left < right:
                s = nums[left] + nums[right]
                if s == find_num:
                    item = [num, nums[left], nums[right]]
                    left += 1
                    right -= 1
                    res.append(item)
                    # VS if left < right and nums[left] == nums[left-1] and nums[right] == nums[right+1]
                    # 三个条件判断 是有bug的
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
                elif s < find_num:
                    left += 1
                else:
                    right -= 1
        return res


# 另外学习的函数
# map 将 set 转化为 list
demo = set()
demo.add((1, 3, 6))
demo.add((2, 6, 9))
reverted = list(map(list, demo))

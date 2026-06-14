# 移动零
# https://www.douyin.com/user/self/search/%E7%A7%BB%E5%8A%A8%E9%9B%B6?modal_id=7566080792154082569&type=general
# start_index 记录零元素的索引位置
# idx 记录当前遍历到的元素索引
# 双指针


def moveZeroes(nums: list[int]):
    start_index = 0

    for idx, num in enumerate(nums):
        if num != 0:
            nums[start_index], nums[idx] = num, nums[start_index]
            start_index += 1

    return nums


n = moveZeroes([2, 0, 1, 0, 3, 12])
print(n)

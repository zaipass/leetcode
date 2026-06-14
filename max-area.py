def maxArea (nums: list[int]) -> int:
    if not nums:
        return 0

    max_area = 0
    left, right = 0, len(nums) - 1
    while left < right:
        height = min(nums[left], nums[right])
        width = right - left
        area = height * width
        max_area = max(max_area, area)

        if nums[left] < nums[right]:
            left += 1
        else:
            right -= 1

    return max_area
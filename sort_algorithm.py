import time
import math
import random


def bubble_sort(nums):
    print('Bubble Sort:')
    lens = len(nums)
    for i in range(lens - 1):  # 对lens个元素只需要遍历lens-1次
        for j in range(lens - i - 1):  # 第i次排序时，已经排好了i个元素，所以只需要对剩下的lens-i个元素进行排序，需要比较lens-i-1次
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]


def selection_sort(nums):
    print('Selection Sort:')
    length = len(nums)
    for i in range(length - 1):
        min_idx = i
        for j in range(i + 1, length):
            if nums[j] < nums[min_idx]:
                min_idx = j
            # print('step:', nums)
        nums[i], nums[min_idx] = nums[min_idx], nums[i]


def insert_sort(nums):
    print('Insert Sort:')
    length = len(nums)
    for i in range(1, length):
        pred_idx = i - 1
        cur = nums[i]
        while pred_idx >= 0 and nums[pred_idx] > cur:
            nums[pred_idx + 1] = nums[pred_idx]
            pred_idx -= 1
        nums[pred_idx + 1] = cur


def _merge(left, right):
    sorted_nums = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_nums.append(left[i])
            i += 1
        else:
            sorted_nums.append(right[j])
            j += 1

    sorted_nums.extend(left[i:])
    sorted_nums.extend(right[j:])

    return sorted_nums


def merge_sort(nums):
    length = len(nums)
    if length < 2:
        return nums
    mid = math.floor(length / 2)
    left_nums = merge_sort(nums[:mid])
    right_nums = merge_sort(nums[mid:])
    return _merge(left_nums, right_nums)


def quick_sort(nums):
    """
    每次选取一个数作为轴，将剩下的数字按照与轴的大小关系分成左右两组，比轴小的分为less组，比轴大的分为more，
    递归实现，最后将less，中轴，more合并，得到排序后的数组
    :param nums: List[int]
    :return: List[int]
    """
    length = len(nums)
    if length < 2:
        return nums
    pivot = nums[0]
    less = [x for x in nums if x < pivot]
    mid = [x for x in nums if x == pivot]
    more = [x for x in nums if x > pivot]
    return quick_sort(less) + mid + more


if __name__ == '__main__':
    num_list = [random.randint(0, 100) for _ in range(0, 8)]
    print('original nums:', num_list)
    start_time = time.time()

    # bubble_sort(num_list)
    # selection_sort(num_list)
    # insert_sort(num_list)
    # out = merge_sort(num_list)
    out = quick_sort(num_list)

    print('use time:', time.time() - start_time)
    print('sorted nums:', out)

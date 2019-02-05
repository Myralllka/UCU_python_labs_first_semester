import time
import random
import copy


def linear_search(line, element):
    for i in range(len(line)):
        if line[i] == element:
            return i
    return -1


def selection_sort(line):
    for i in range(len(line)):
        min_element = i
        for j in range(i + 1, len(line)):
            if line[j] < line[i]:
                min_element = j
        line[i], line[min_element] = line[min_element], line[i]
    return line


def binary_search(line, element):
    l_index = 0
    r_index = len(line)
    while True:
        if r_index - l_index == 0:
            if line[l_index] == element:
                return l_index
            else:
                return -1
        middle_index = (r_index + l_index) // 2
        if element > line[middle_index]:
            l_index = middle_index
        elif element < line[middle_index]:
            r_index = middle_index
        else:
            return middle_index


def merge(nums1, nums2):
    result = []
    i = 0
    minn = min(len(nums1), len(nums2))
    while i < minn:
        if nums1[0] > nums2[0]:
            result.append(nums2.pop(0))
        else:
            result.append(nums1.pop(0))
        if len(nums1) == 0:
            result.extend(nums2)
            break
        elif len(nums2) == 0:
            result.extend(nums1)
            break
    return result


def merge_sort(nums):
    n = len(nums)
    if n > 1:
        m = n // 2
        nums1, nums2 = nums[:m], nums[m:]
        nums1 = merge_sort(nums1)
        nums2 = merge_sort(nums2)
        result = []
        result = merge(nums1, nums2)
        return result
    else:
        return nums


def quick_sort(line):
    if len(line) <= 1:
        return line
    l_line, m_line, r_line = [], [random.choice(line)], []
    for n in line:
        if n < m_line[0]:
            l_line.append(n)
        elif n > m_line[0]:
            r_line.append(n)
    return quick_sort(l_line) + m_line + quick_sort(r_line)


def quicksort(line):
    if len(line) <= 1:
        return line
    else:
        q = random.choice(line)
    l_nums = [n for n in line if n < q]
    e_nums = [q] * line.count(q)
    r_nums = [n for n in line if n > q]
    return quicksort(l_nums) + e_nums + quicksort(r_nums)

# a = [random.randrange(100000) for i in range(5000000)]
a = [1, 3, 2, 3, 9, 0, 1, 0]
# a = [4, 1, 6, 3, 2, 7, 8]
# time1 = time.time()
# selection_sort(a)
# print(time.time() - time1)
# time1 = time.time()
print(quicksort(a))
# print(time.time() - time1)
# time1 = time.time()
# sorted(a)
# print(time.time() - time1)

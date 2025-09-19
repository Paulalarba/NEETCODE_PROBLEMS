# Contains Duplicate
# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

# Example 1:

# Input: nums = [1, 2, 3, 3]

# Output: true

# Example 2:

# Input: nums = [1, 2, 3, 4]

# Output: false
# solution 1 brute force: it is good way to check if the number is budlacate but it is slow because it checks
# the number 1 by 1

def bruteforce(nums):
    n = len(nums)
    for i in range(n):
        for j in range(i +1, n):
            if nums[i] == nums[j]:
                return True
    return False
print(bruteforce([1, 2, 3, 4, 1]))
print(bruteforce([1, 2, 3, 4, 5]))

# best way is using the hashset: hash set basically check if the number is already seen
def hashset(num):
    seen = set()
    for i in num:
        if i in seen:
            return True
        seen.add(i)
    return False
print(hashset([1, 2, 3, 4, 1]))
print(hashset([1, 2, 3, 4, 5]))


def brutforce2(nums):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] == nums[j]:
                return True
    return False

print(brutforce2([1, 2, 3, 4, 1]))

def hashset2(nums):
    x = set()
    for i in nums:
        if i in x:
            return True
        x.add(i)
    return False
print(hashset2([1, 2, 1]))
# Arrays Question #1 - Two Sum of a Given Array

def two_sum(nums, target):

    for i in range(0, len(nums)):
        num_to_find = target - nums[i]

        for j in range(i+1, len(nums)):
            if num_to_find == nums[j]:
                return [i, j]
    
    return None  # No solution

# Time complexity: O(n^2)
# Space complexity: O(1)
print("Brute force solution...")
print(two_sum([1,3,7,9,2], 11))


def improved_two_sum(nums, target):
    result = {}

    for i in range(0, len(nums)):
        value = result.get(nums[i])
    
        if value is not None:
            return [value, i]
        else:
            num_to_find = target - nums[i]
            result[num_to_find] = i
        
    return None  # No solution

# Time complexity: O(n)
# Space complexity: O(n)
print("Optimal solution...")
print(improved_two_sum([1,3,7,9,2], 11))

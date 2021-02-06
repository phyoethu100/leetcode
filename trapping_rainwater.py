# Arrays Question #3 - Trapping Rainwater

def trapped_rainwater(heights):

    total_water = 0
    
    for p in range(0, len(heights)):
        left_p = p
        right_p = p
        max_left = 0
        max_right = 0

        while left_p >= 0:
            max_left = max(max_left, heights[left_p])
            left_p -= 1

        while right_p < len(heights):
            max_right = max(max_right, heights[right_p])
            right_p += 1

        current_water = min(max_left, max_right) - heights[p]

        if current_water >= 0: 
            total_water += current_water
    
    return total_water

# Time complexity: O(n^2)
# Space complexity: O(1)
print("Brute force solution...")
print(trapped_rainwater([0,1,0,2,1,0,3,1,0,1,2]))


def improved_trapped_rainwater(heights):

    total_water = 0
    left = 0
    right = len(heights) - 1
    max_left = 0
    max_right = 0

    while left < right:
        if heights[left] <= heights[right]:
            if heights[left] >= max_left:
                max_left = heights[left]
            else:
                total_water += max_left - heights[left]
            left += 1
        else:
            if heights[right] >= max_right:
                max_right = heights[right]
            else:
                total_water += max_right - heights[right]
            right -= 1
        
    return total_water
            
# Time complexity: O(n)
# Space complexity: O(1)
print("Optimal solution...")
print(improved_trapped_rainwater([0,1,0,2,1,0,3,1,0,1,2]))
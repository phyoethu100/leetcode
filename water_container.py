# Arrays Question #2 - Container with Most Water

def max_water(heights):

    max_area = 0

    for i in range(0, len(heights)):
        for j in range(i+1, len(heights)):
            
        #   Built-in min function: height = min(heights[i], heights[j])
            if heights[i] > heights[j]:
                height = heights[j]
            else:
                height = heights[i]

            width = j - i
            current_area = height * width

        #   Built-in max function: max_area = max(max_area, current_area)  
            if current_area > max_area:
                max_area = current_area
    
    return max_area

# Time complexity: O(n^2)
# Space complexity: O(1)
print("Brute force solution...")
print(max_water([7,1,2,3,9]))


def improved_max_water(heights):

    i = 0
    j = len(heights) - 1
    max_area = 0

    while i < j:
    #   Built-in min function: height = min(heights[i], heights[j])
        if heights[i] > heights[j]:
            height = heights[j]
        else:
            height = heights[i]

        width = j - i
        current_area = height * width

    #   Built-in max function: max_area = max(max_area, current_area)  
        if current_area > max_area:
            max_area = current_area

        if heights[i] <= heights[j]:
            i += 1
        else:
            j -= 1 
    
    return max_area

# Time complexity: O(n)
# Space complexity: O(1)
print("Optimal solution...")
print(improved_max_water([7,1,2,3,9]))
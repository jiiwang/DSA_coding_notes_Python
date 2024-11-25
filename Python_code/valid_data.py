def determine_date_components(a, b, c):
    # Define the list of nums
    nums = [a, b, c]
    
    # Determine the year (year has to be the largest value)
    year = max(nums)
    if year < 1000 or year > 9999:
        return "Invalid date components"
    
    # Remaining two nums to determine day and month
    nums.remove(year)

    ans = []

    # Determine which is the month and which is the day
    # first check if there is ambiguous month and day
    if 1 <= nums[0] <= 12 and 1 <= nums[1] <= 12:
        if nums[0] != nums[1]:
            ans.append(str(year) + '-' + str(nums[0]) + '-' + str(nums[1]))
            ans.append(str(year) + '-' + str(nums[1]) + '-' + str(nums[0]))
        else:
            ans.append(str(year) + '-' + str(nums[0]) + '-' + str(nums[1]))
        
        return ans

    if 1 <= nums[0] <= 12 and 1 <= nums[1] <= 31:
        month, day = nums[0], nums[1]
        ans.append(str(year) + '-' + str(month) + '-' + str(day))
    elif 1 <= nums[1] <= 12 and 1 <= nums[0] <= 31:
        month, day = nums[1], nums[0]
        ans.append(str(year) + '-' + str(month) + '-' + str(day))
    else:
        return "Invalid date components"

    return ans

# Example usage:
a, b, c = 2023,20,9  # year, month, day in any order
print(determine_date_components(a, b, c))  

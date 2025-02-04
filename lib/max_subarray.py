
def max_sub_array(nums):
    """ Returns the max subarray of the given list of numbers.
        Returns 0 if  nums is None or an empty list.
        Time Complexity: O(n)
        Space Complexity: O(1)
    """
    if not nums:
        return 0
    
    if max(nums) < 0:
        return max(nums)
# Kadane's Algorithm
    max_so_far = 0
    max_ending_here = 0

    for i in range(len(nums)):
        max_ending_here = max_ending_here + nums[i]
        if(max_ending_here < 0):
            max_ending_here = 0
        if(max_so_far < max_ending_here):
            max_so_far = max_ending_here
    return max_so_far

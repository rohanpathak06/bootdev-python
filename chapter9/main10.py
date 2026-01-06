"""ssignment
Our players want a way to see their strongest attack from their last combat. Some enemies may be buffed to absorb either magic or melee attacks as health, which result in negative damage. Let's add another function to analyze data from our combat log.

Complete the find_max function. It takes as input a list of integers, nums, and returns an integer.

max_so_far is initialized as negative infinity.
Compare each number in nums to max_so_far. If any number is larger than max_so_far, replace max_so_far with that value.
Return max_so_far. If nums is empty, return negative infinity.
Here's an example of how your find_max function should work:"""

def find_max(nums):
    max_so_far = float("-inf")
    for i in nums:
        if i > max_so_far:
            max_so_far = i
    return max_so_far
    
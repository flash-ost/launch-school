"""
Given the following list:

numbers = [1, 2, 3, 4, 5]
Write two functions to fetch the sixth element from the list: one using the LBYL approach and another using the AFNP approach. In both cases, the function should return None when the element isn't found.
"""

# # LBYL
# def fetch_sixth(nums):
#     return nums[5] if len(nums) >= 6 else None

# AFNP
def fetch_sixth(nums):
    try:
        return nums[5]
    except IndexError:
        return None

numbers = [1, 2, 3, 4, 5]

print(fetch_sixth(numbers))
from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
  # Your Codes#
  for i in range( len(nums) ):
    for j in range( i+1, len(nums) ):
      if target==nums[i]+nums[j]:
        return [i, j]

  # Do not use input() or print() in your function#
  # Inputs (nums, target)  will given as arguments and the output as #
  # return value return
  # Your Answer

# print( twoSum([2, 7, 11, 15],9))
#print( twoSum([3, 2, 4],6))
#print( twoSum([3, 3],6))


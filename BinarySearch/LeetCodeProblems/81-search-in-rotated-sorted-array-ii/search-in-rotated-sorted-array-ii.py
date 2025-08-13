class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                return True

            # When we can't determine which part is sorted due to duplicates
            if nums[low] == nums[mid] == nums[high]:
                low += 1
                high -= 1
            # Left part is sorted
            elif nums[low] <= nums[mid]:
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            # Right part is sorted
            else:
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return False

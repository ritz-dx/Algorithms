class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1,-1]

        def leftSearch():
            low = 0
            high = len(nums)-1
            first = -1
            while low<=high:
                mid = (low+high)//2
                if nums[mid] < target:
                    low = mid + 1
                elif nums[mid] >target:
                    high = mid - 1
                else:
                    first = mid
                    high = mid -1
            return first

        def rightSearch():
            low = 0
            high = len(nums)-1
            last = -1
            while low <= high:
                mid = (low + high)//2
                if nums[mid] < target:
                    low = mid + 1
                elif nums[mid] > target:
                    high = mid - 1
                else:
                    last = mid
                    low = mid + 1

            return last
            
        
        return [leftSearch(),rightSearch()]
                


                
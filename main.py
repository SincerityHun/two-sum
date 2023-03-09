class sumUp:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        answer = list()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    answer.append(i)
                    answer.append(j)
        return answer


nums = [3, 3]
target = 6
answer = sumUp()
print(answer.twoSum(nums, target))

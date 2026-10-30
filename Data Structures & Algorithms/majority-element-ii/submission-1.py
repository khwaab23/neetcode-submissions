class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # We keep the first possible majority candidate.
        candidate1 = None

        # We keep the second possible majority candidate.
        candidate2 = None

        # This count tracks the strength of candidate1.
        count1 = 0

        # This count tracks the strength of candidate2.
        count2 = 0

        # First pass: find the two possible candidates.
        for num in nums:

            # If the current number matches candidate1, we increase its count.
            if candidate1 == num:
                count1 += 1

            # If the current number matches candidate2, we increase its count.
            elif candidate2 == num:
                count2 += 1

            # If candidate1 has no active count, we replace it with the current number.
            elif count1 == 0:
                candidate1 = num
                count1 = 1

            # If candidate2 has no active count, we replace it with the current number.
            elif count2 == 0:
                candidate2 = num
                count2 = 1

            # If the number matches neither candidate, it cancels out both candidates once.
            else:
                count1 -= 1
                count2 -= 1

        # We create the result list where we will store the final valid answers.
        result = []

        # Second pass: verify candidate1 by counting its actual frequency.
        actual_count1 = nums.count(candidate1)

        # Second pass: verify candidate2 by counting its actual frequency.
        actual_count2 = nums.count(candidate2)

        # If candidate1 appears more than n / 3 times, it is a valid answer.
        if actual_count1 > n // 3:
            result.append(candidate1)

        # If candidate2 is different from candidate1 and appears more than n / 3 times, it is valid.
        if candidate2 != candidate1 and actual_count2 > n // 3:
            result.append(candidate2)

        # Finally, we return all valid majority elements.
        return result
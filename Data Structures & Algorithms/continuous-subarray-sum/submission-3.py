class Solution:
    def checkSubarraySum(
        self,
        nums,
        k
    ):

        # I remember the earliest index where
        # each remainder first appeared
        remainder_map = {
            0: -1
        }

        # I maintain the running prefix sum
        prefix_sum = 0

        # I process each element once
        for i, num in enumerate(nums):

            # I extend the current prefix
            prefix_sum += num

            # Equal remainders imply the
            # subarray sum is divisible by k
            remainder = prefix_sum % k

            # If I've seen this remainder before,
            # I check whether the subarray is valid
            if remainder in remainder_map:

                if (
                    i - remainder_map[remainder]
                    >= 2
                ):
                    return True

            # I keep only the first occurrence
            # because it gives the longest subarray
            else:
                remainder_map[
                    remainder
                ] = i

        return False
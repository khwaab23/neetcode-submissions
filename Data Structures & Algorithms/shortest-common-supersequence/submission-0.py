# class Solution:
#     def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
class Solution:
    def shortestCommonSupersequence(
        self,
        str1: str,
        str2: str
    ) -> str:

        # I need both lengths to define the DP states
        m = len(str1)
        n = len(str2)

        # I store the LCS length for every prefix pair
        dp = [
            [0] * (n + 1)
            for _ in range(m + 1)
        ]

        # I build smaller prefix answers before larger ones
        for i in range(1, m + 1):
            for j in range(1, n + 1):

                # A matching character extends the common subsequence
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = (
                        1 + dp[i - 1][j - 1]
                    )

                # Otherwise I keep the better previous prefix
                else:
                    dp[i][j] = max(
                        dp[i - 1][j],
                        dp[i][j - 1]
                    )

        # I reconstruct the answer from the completed table
        i = m
        j = n
        result = []

        # I include characters while both strings remain
        while i > 0 and j > 0:

            # A common character should appear only once
            if str1[i - 1] == str2[j - 1]:
                result.append(
                    str1[i - 1]
                )
                i -= 1
                j -= 1

            # Moving upward means this str1 character is needed
            elif dp[i - 1][j] >= dp[i][j - 1]:
                result.append(
                    str1[i - 1]
                )
                i -= 1

            # Moving left means this str2 character is needed
            else:
                result.append(
                    str2[j - 1]
                )
                j -= 1

        # Any remaining str1 characters must still be included
        while i > 0:
            result.append(
                str1[i - 1]
            )
            i -= 1

        # Any remaining str2 characters must still be included
        while j > 0:
            result.append(
                str2[j - 1]
            )
            j -= 1

        # I built the answer backward, so I reverse it
        return "".join(
            reversed(result)
        )
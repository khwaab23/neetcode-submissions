class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n=len(days)
        maxday=days[-1]
        minday=days[0]
        dp=[0]*(maxday+1)
        # dp[0]=0
        travel_days=set(days)

        for i in range(minday,maxday+1):
            if i not in travel_days:
                dp[i]=dp[i-1]
            else:
                dp[i]=dp[i-1]+costs[0]
                dp[i]=min(dp[i],(dp[i-7] if i-7>=0 else 0) +costs[1])
                dp[i]=min(dp[i],(dp[i-30] if i-30>=0 else 0) +costs[2])
        
        return dp[maxday]


        n = len(days)
        maxDay, minDay = days[-1], days[0]

        # DP array for days from minDay to maxDay
        dp = [0] * (maxDay + 1)
        travelDays = set(days)

        for i in range(minDay, maxDay + 1):
            if i not in travelDays:
                dp[i] = dp[i - 1]
            else:
                dp[i] = dp[i - 1] + costs[0]  # 1-day pass
                dp[i] = min(dp[i], (dp[i - 7] if i - 7 >= 0 else 0) + costs[1])  # 7-day pass
                dp[i] = min(dp[i], (dp[i - 30] if i - 30 >= 0 else 0) + costs[2])  # 30-day pass

        return dp[maxDay]
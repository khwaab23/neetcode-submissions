class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        maxfruit=0
        l=0
        fruit={}
        res=0
        for r in range(len(fruits)):
            fruit[fruits[r]] = fruit.get(fruits[r], 0) + 1
            res+=1
            
            while len(fruit)>2:
                fruit[fruits[l]] -= 1
                if fruit[fruits[l]] == 0:
                    del fruit[fruits[l]]
                l+=1
                res-=1
            maxfruit=max(res,maxfruit)
        return maxfruit
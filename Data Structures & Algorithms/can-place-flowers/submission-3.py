class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        m=len(flowerbed)
        i=0

        while i<m:
            
            
            if flowerbed[i]==0 and (i == 0 or flowerbed[i-1] == 0) and (i == m-1 or flowerbed[i+1] == 0):
                flowerbed[i]=1
                n-=1
            
            if n<=0:
                return True
            i+=1
            
        return False
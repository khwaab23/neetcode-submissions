class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        
        l=0
        changes=0
        minchanges=float('inf')

        for r in range(len(blocks)):

            
            
            
            if blocks[r]=="W":
                changes+=1
            
            if r-l+1==k:
                minchanges=min(changes,minchanges)
                if blocks[l]=="W":
                    changes-=1
                l+=1
        return minchanges
            

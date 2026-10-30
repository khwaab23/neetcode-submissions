class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count=Counter(arr1)
        res=[]
        end=[]
        for num in arr1:
            if num not in arr2:
                end.append(num)
        end.sort()
        for num in arr2:
            while count[num]:
                count[num]-=1
                res.append(num)

        return res+end


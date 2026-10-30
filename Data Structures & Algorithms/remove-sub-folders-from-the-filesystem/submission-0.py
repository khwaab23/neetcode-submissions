class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        res=[]
        fset=set(folder)
        for f in folder:
            res.append(f)
            for i in range(len(f)):
                if f[i]=="/" and f[:i] in fset:
                    res.pop()
                    break
        return res
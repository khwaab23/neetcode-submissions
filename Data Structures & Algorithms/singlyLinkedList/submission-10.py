class listnode:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None
    
    def get(self, index: int) -> int:
        cursor = self.head
        i = 0 
        while (cursor):
            if(i == index):
                return cursor.val
            cursor = cursor.next
            i+=1
        return -1


    def insertHead(self, val: int) -> None:
        newnode = listnode(val)
        newnode.next = self.head
        self.head = newnode

    def insertTail(self, val: int) -> None:
        newnode = listnode(val)
        if not self.head:
            self.head = newnode
            return
        cursor = self.head
        while cursor.next:
            cursor = cursor.next
        cursor.next = newnode

        

    def remove(self, index: int) -> bool:
        if not self.head:
            return False
        if index == 0:
            self.head = self.head.next
            return True
        cursor = self.head
        i = 0 
        while (cursor and cursor.next):
            if(i == index-1):
                cursor.next = cursor.next.next
                return True
            cursor = cursor.next
            i+=1
        return False


    def getValues(self) -> List[int]:
        arr = []
        cur = self.head
        while cur:
            arr.append(cur.val)
            cur = cur.next
        return arr
        

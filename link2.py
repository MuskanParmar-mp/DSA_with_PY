class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linklist:
    def __init__(self):
        self.head=None
    def Insert_begin(self,data):
        newnode = node(data)
        if self.head is None:
            self.head= newnode
            return
        newnode.next=self.head
        self.head=newnode


    def traverse(self):
        if self.head is None:
            print("linklist is empyt")
            return

        cur=self.head
        while cur:
            print(cur.data,end="->")
            cur = cur.next
        print("None")        
            
l1 = linklist()
l1.Insert_begin(200)            
        
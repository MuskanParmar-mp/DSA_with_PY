#without parameter and no return value
'''def show():
    print("1000")

show() '''   



#with parameter and no return value
'''def show(n):
    print("hello")'''

 


#without parameter and return value
'''def price():
    return 1000

print(price()+2000)'''


#with parameter and return value
'''def sum(a1,a2):
    return a1+a2

print(sum(10,20)*20)''' 



class node:
    def __init__(self,data):
        self.data=data
        self.next=None

    def traverse(self,head):
        cur = head 
        while cur!=None:
            print(cur.data,end="->")
            cur = cur.next
        print("None")      

node1=node(10)       
node2=node(20) 
node3=node(30)
node4=node(40) 
node1.next=node2
node2.next=node3
node3.next=node4
h=node1
node1.traverse(h)
# print(node1.next.data)
# print(node1.next.next.data)
# print(node1.next.next.next.data)
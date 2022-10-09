class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def insert(self,head,data):
        newnode = Node(data)
        
    #The head argument is null for an empty list.       
        if head == None:
            head = newnode
            return newnode
        temp = head
        while temp.next:
            temp = temp.next
        temp.next = newnode
        return head  
        
mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
mylist.display(head); 	  

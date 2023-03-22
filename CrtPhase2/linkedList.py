class Node:
    def __init__(self,value):
        self.data=value
        self.next=None
class LinkedList:
    def add_ele_beg(self,value,head):
        new_node=Node(value)
        new_node.next=head
        head=new_node
        return head
    def add_element(self,head,value):
        new_node=Node(value)
        temp = head
        while temp.next != None:
            temp = temp.next
        temp.next=new_node
    def remove_element(self,head):
        temp=head
        while temp.next.next!= None:
            temp=temp.next
        temp.next=None
    def insert_element(self,head,value,index):
        new_node=Node(value)
        curr=head
        prev=None
        while index!=0:
            prev=curr
            curr=curr.next
            index=index-1
        prev.next=new_node
        new_node.next=curr
    def print_list(self,head):
        temp=head
        while temp!=None:
            print(temp.data,end='->')
            temp=temp.next
        print()
    def search_element(self,value):pass
obj=LinkedList()
head=Node(10)
obj.add_element(head,20)
obj.add_element(head,30)
obj.add_element(head,40)
obj.add_element(head,50)
obj.remove_element(head)
obj.print_list(head)
obj.insert_element(head,100,2)
obj.print_list(head)
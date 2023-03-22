class Node:
    def __init__(self,value):
        self.data=value
        self.next=None
class LinkedList:
    def add_element(self,head,value):
        new_node=Node(value)
        temp = head
        while temp.next != None:
            temp = temp.next
        temp.next=new_node
    def print_list(self,head):
        temp=head
        while temp!=None:
            print(temp.data,end='->')
            temp=temp.next
        print()
    def num_of_primes(self):
        count=0
        prime=False
        temp=head
        while temp.next!=None:
            x=temp.data
            for i in range(2,x):
                if x%i==0:
                    break
                else:
                    prime=True

            temp=temp.next
        return count
obj=LinkedList()
head=Node(10)
obj.add_element(head,2)
obj.add_element(head,3)
obj.add_element(head,4)
obj.add_element(head,5)
print(obj.num_of_primes())

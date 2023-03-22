class Queue:
    arr=[]
    def enqueue(self,ele):
        self.arr.append(ele)
    def dequeue(self):
        return self.arr.pop(0)
    def queue_peek(self):
        return self.arr[-1]
    def print_queue(self):
        print(self.arr)
q1=Queue()
q1.enqueue(1)
q1.enqueue(2)
q1.enqueue(3)
q1.enqueue(4)
q1.print_queue()
q1.dequeue()
q1.print_queue()
print(q1.queue_peek())

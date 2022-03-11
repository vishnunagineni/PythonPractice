class Node():
    def __init__(self,d):
        self.data=d
        self.next=None

class Stack():
    def __init__(self):
        self.head=Node("head")
        self.size=0

    def __str__(self):
        cur=self.head.next
        out=""
        while cur:
            out+=str(cur.data)+"->"
            cur=cur.next
        return out[:-2]
    def get_size(self):
        return self.size

    def isEmpty(self):
        return self.size==0

    
    def push(self,a):
        n=Node(a)
        n.next=self.head.next
        self.head.next=n
        self.size+=1

    
    def pop(self):
        if self.isEmpty():
            raise Exception("Popping from empty stack!!!!")
        temp=self.head.next
        self.head.next=self.head.next.next
        self.size-=1
        return temp.data
    
    def peek(self):
        if self.isEmpty():
            raise Exception("Peeking from Empty stack!!!!")
        return self.head.next.data

if __name__=="__main__":
    s=Stack()
    s1=Stack()
    for i in range(1,12):
        s.push(i)
        if i%2==0:
            s1.push(i)
    print(f"Stack1:{s}")
    print(f"Stack2:{s1}")
    for _ in range(1,14):
        t=s.pop()
        if t%2==0:
            x=s1.pop()
            print(x)
        print(f"Popped element:{t}")
    
    print(f"Stack1 after popping elements: {s}")
    print(f"Stack2 after popping elements: {s1}")

            




    
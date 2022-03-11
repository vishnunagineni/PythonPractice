class person:
    def __init__(self,name,h,w):
        self.name=name
        self.height=h
        self.weight=w
    def findavgheight(l):
        sum=0
        for i in l:
            sum+=i.height
        return sum/len(l)
    def personmorethanavg(l,avg):
        for i in l:
            if i.height > avg:
                print(i.name)

l=[]
n=int(input("Enter number of persons"))
for i in range(0,n):
    name=input("name?")
    height=float(input("Height?"))
    weight=int(input("Weight?"))
    l.append(person(name,height,weight))
avg=person.findavgheight(l)
print("Average height is {0}".format(avg))

person.personmorethanavg(l,avg)


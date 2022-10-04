class Difference:
    def __init__(self, a):
        self.__elements = a
    
    def computeDifference(self):
        mx = 0
        mn = 101
        for i in a:
            if i < mn:
                mn = i
        
        for i in a:
            if i > mx:
                mx = i
                
        self.maximumDifference = mx - mn
        

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)

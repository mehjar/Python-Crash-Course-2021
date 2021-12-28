#Tuple
a = (1,2,3,4)
print(type(a))

#List
a = [1,2,3,4]
print(type(a))

a = (1,2.4,3.3,5.2)
print a

a = [1,2.4,3.3,5.2]
print a

print a[-1:]
print a[-2:]
print a[-3:]
print a[-4:]

a = [1,2.4,3.3,5.2]
#a.append(100)  Append is not available for Tuples
#a(1) = 200 Tuples are immutable
print(a)
a[:] = []
print a

a = [1,2,3,4,5]
b = [7,8,9,10]
#List functions
a.append(6)
a.extend(b)
a.insert(5,5.5)
#a.remove(5.50)
a.pop(1)
ind = a.index(5.50)+1
a.reverse()
a.sort()
    #This is a useful function. This plays the role of find. Will be interesting to see how it functions when dealing with more complex floats.
print(a,ind,a.count(3),len(a))

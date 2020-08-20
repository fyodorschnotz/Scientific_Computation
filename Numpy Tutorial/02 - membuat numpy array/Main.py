import numpy as np

#membuat vector
a = np.array([1,2,3,4,5])
b = np.array([1.5,2.5,5,6,7])

#membuat vector dengan range
c = np.arange(1,10,2)

# membuat linear space / linspace
d = np.linspace(1,10,4)

#array multidimensi/matrix
e = np.array([ (1,2,3,) , (4,5,6) ])

# matrix dengan nilai nol
f = np.zeros((5,5))

#matrix dengan nilai satu
g = np.ones((5,5))

# matrix identitas
h = np.identity(5)
h2 = np.eye(5)
#display

print(a)
print(b)
print(c)
print(d)
print(e + 1)
print(f)
print(g)
print(h)
print(2)
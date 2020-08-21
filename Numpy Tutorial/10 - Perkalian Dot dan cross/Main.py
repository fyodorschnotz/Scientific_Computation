import numpy as np

a = np.array([1,3,2])
b = np.array([2,1,2])

# perkalian dot
c = np.dot(a,b)

# perkalian cross
a = np.array([1,2,0])
b = np.array([2,1,0])

c= np.cross(a,b)
d = np.cross(b,a)

print(d)

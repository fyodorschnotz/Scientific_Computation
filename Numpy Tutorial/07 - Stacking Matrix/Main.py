import numpy as np

a = np.array([1,2,3])
b = np.array([4,5,6])

amat = np.zeros((2,3))
bmat = np.zeros((2,3))
# stacking matrix, menumpuk matrix

c = np.hstack((a,b)) #hstack berfungsi untuk menambahkan array berdasarkan horizontal
d = np.hstack((a,b)) #vstack berfungsi untuk menambahkan array berdasarkan vertical

cmat = np.hstack((amat,bmat))
dmat = np.vstack((amat,bmat))

print(cmat)
import numpy as np

a = np.array((
            [1,2,3],
            [4,5,6]
))

print('matrix dengan ukuran:', a.shape)
#transpose matrix
print('transpose matrix dari a:')
print(a.transpose())
print('\n')
print(np.transpose(a))
print('\n')
print(a.T)

# flatten array, vector baris
print('flatten matrix a:')
print(a.ravel())
print(np.ravel(a))

#reshape matrix
print('reshape matrix a:')
print(a.reshape(6,1))

#resize matrix
print('resize matrix a:')
print(a.resize(3,2)) #merubah nilai yang diresize
print(a)
print(a.shape)
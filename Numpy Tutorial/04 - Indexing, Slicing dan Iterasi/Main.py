import numpy as np

a = np.arange(10)**2
print(a)

#mengambil nilai
print('elemen ke 1 dari a adalah', a[0])
print('elemen ke 1 dari a adalah', a[6])
print('elemen ke 1 dari a adalah', a[-1])

#slicing
print('elemen dari 1-6 adalah',a[0:6]) #
print('elemen dari 4 sampai akhir', a[3:])
print('elemen dari awal sampe 5', a[:5])

#iterasi
for i in a:
    print('value =', i)
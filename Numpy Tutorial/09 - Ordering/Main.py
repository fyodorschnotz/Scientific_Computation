import numpy as np

a = np.floor(np.random.randn(1,6)*10) #syntax untuk ngeluarin array random

print(a)

print('nilai max dari a=', a.max())
print('posisi max dari a =', a.argmax()) #ngambil posisi max
print('nilai min dari a=', a.min())
print('posisi min dari a =', a.argmin()) #ngambil posisi max

#mengurutkan nilai dari a
print('mengurutkan nilai a:')
print(np.sort(a))
print(np.argsort(a))
import numpy as np

#~ NumPy Format

a = np.array([
[ 10 , 20 , 30 ],
[ 40 , 50 , 60 ],
[ 70 , 80 , 90 ],
[ 100 , 110 , 120 ]
])

#>> Saving data to a npy array
np.save("myarray.npy", a)

#>> Loading data
a = np.load('myarray.npy')

print(a)

"""
[[ 10  20  30]
 [ 40  50  60]
 [ 70  80  90]
 [100 110 120]]
"""

#~ CSV Format
#>> We use savetxt and loadtxt function for that

np.savetxt("myarray.csv", a)

a = np.loadtxt("myarray.csv")

print(a)

"""
[[ 10.  20.  30.]
 [ 40.  50.  60.]
 [ 70.  80.  90.]
 [100. 110. 120.]]
"""
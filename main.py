#numpy can be used to store all kinds of data
import numpy as np


# # a = np.array([1,2,3],dtype='int16')
# # # print(a)
# # b = np.array([[9.0,8.0,7.0],[6.0,5.0,4.0]])
# # # print(b)

# # print(a.ndim)
# # print(b.shape)

# # print(a.dtype)

# # print(a.itemsize)

# # print(a.size)

# # a = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])

# # print(a[1,5])

# # print(a[0, :])

# # print(a[0, 1:6:2])

# # a[1,5] = 20
# # print(a)


# a =np.zeros((2,3))

# print(a)



# b =np.ones((4,2,2),dtype='int32')

# print(b)

# c = np.full_like(a,4)
# print(c)

# d = np.random.rand(4,2)
# print(d)



# arr = np.array([[1,2,3]])
# r1 = np.repeat(arr,3,axis = 0)
# print(r1)

# output = np.ones((5,5))
# print(output)

# z = np.zeros((3,3))
# z[1,1] = 9
# print(z)


# a = np.array([1,2,3])
# b = a.copy()
# b[0] = 100

# print(a)




# a = np.array([1,2,3,4])
# print(a)

# print(a+3)

# b = np.array([2,2,4,4])
# print(a + b)


# a = np.ones((2,3))
# b = np.full((3,2),2)

# np.matmul(a,b)

# print(a)



# stats = np.array([[1,2,3],[4,5,6]])





# before = np.array([[1,2,3,4],[5,6,7,8]])
# print(before)
# after = before.reshape(8,1)
# print(after)



# v1 = np.array([1,2,3,4])
# v2 = np.array([5,6,7,8])
# print(np.vstack([v1,v2]))



from numpy import random
 
# x = random.rand(100)
# print(100)
# y = random.randint(100, size=(3,5))

# print(y)

# z = random.choice([3,5,7,9],p=[0.1, 0.3, 0.6, 0.0],size=(3,5))
# print(z)


arr = np.array([1, 2, 3, 4, 5])



# print(random.permutation(arr))


a = random.normal(loc = 1,scale=2,size=(2,3))

print(a)
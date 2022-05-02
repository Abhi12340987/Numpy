import numpy as np

#pixels are numbers and can be represented by using a list
#an image/pixels of size 5 x 3 can be represented by a list with 3 more lists that have 5 numbers, cuz 5 columns and 3 rows
#list take up alot of memory and not very effcient
#this is solved by numpy

n =np.arange(27)
a = n.reshape(3,9) #two dimensional array
print(a)
p = n.reshape(3,3,3) #three dimensioanl array
print(p)




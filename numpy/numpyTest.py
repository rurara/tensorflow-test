import numpy 

array = numpy.random.rand(4,4)
matArray = numpy.mat(array)
multipleArray = array * matArray

print(array)
print(matArray.I)
print(multipleArray)
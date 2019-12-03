from numpy import *
import operator
import matplotlib
import matplotlib.pyplot as plt


def createDataSet():
	group = array ([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
	labels = ['A', 'A', 'B', 'B']
	return group, labels


group, labels = createDataSet()
print(group)
print(labels)

def classif0(inX, dataSet, labels, k):
	dataSetSize = dataSet.shape[0]
	diffMat = tile(inX, (dataSetSize, 1)) - dataSet
	sqDiffMat = diffMat ** 2
	sqDistances = sqDiffMat.sum(axis = 1)
	distances = sqDistances ** 0.5
	sortedDistIndicies = distances.argsort()
	classCount = {}
	for i in range(k):
		voteIlabel = labels[sortedDistIndicies[i]]
		classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
	sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
	return sortedClassCount[0][0]

def file2Matrix(fileName):
	fr = open(fileName)
	numberOfLines = len(fr.readlines())
	returnMat = zeros((numberOfLines, 3))
	classLabelVector = []
	fr = open(fileName)
	index = 0
	for line in fr.readlines():
		line = line.strip()
		listFromLine = line.split('\t')
		returnMat[index, :] = listFromLine[0:3]
		classLabelVector.append(listFromLine[-1])
		index += 1
	return returnMat, array(classLabelVector, dtype=int32)
	
# print(classif0([0,0], group, labels, 3))
# print(classif0([0,1], group, labels, 3))
# print(classif0([1,0], group, labels, 3))
# print(classif0([1,1], group, labels, 3))	



# print(file2Matrix('datingTestSet.txt'))


datingDataMat, datingDataLabels = file2Matrix('datingTestSet2.txt')
# print(datingDataLabels)
# print(datingDataLabels * 15)

fig = plt.figure()
ax = fig.add_subplot(111)


#챠트 확인하기 
# ax.scatter(datingDataMat[:, 1], datingDataMat[:, 2], 20.0*array(datingDataLabels), 20.0*array(datingDataLabels))
# plt.show()

def autoNorm(dataSet):
	minVals = dataSet.min(0)
	maxVals = dataSet.max(0)
	ranges = maxVals - minVals
	normDataSet = zeros(shape(dataSet))
	m = dataSet.shape[0]
	normDataSet = dataSet - tile(minVals, (m,1))
	normDataSet = normDataSet / tile(ranges, (m, 1))
	return normDataSet, ranges, minVals
	


normMat, ranges, minVals = autoNorm(datingDataMat)

print(datingDataMat)
print(autoNorm(datingDataMat))
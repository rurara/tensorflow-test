import kNN

from numpy import *
import operator
from os import listdir

group, labels = kNN.createDataSet()
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









print(classif0([0,0], group, labels, 3))
print(classif0([0,1], group, labels, 3))
print(classif0([1,0], group, labels, 3))
print(classif0([1,1], group, labels, 3))
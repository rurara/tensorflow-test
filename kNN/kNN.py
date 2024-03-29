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

def classify0(inX, dataSet, labels, k):
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
	
# print(classify0([0,0], group, labels, 3))
# print(classify0([0,1], group, labels, 3))
# print(classify0([1,0], group, labels, 3))
# print(classify0([1,1], group, labels, 3))	



# print(file2Matrix('datingTestSet.txt'))



fig = plt.figure()
ax = fig.add_subplot(111)


#챠트 확인하기 
# ax.scatter(datingDataMat[:, 1], datingDataMat[:, 2], 20.0*array(datingLabels), 20.0*array(datingLabels))
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
	
#데이터 정규화 하기 
# normMat, ranges, minVals = autoNorm(datingDataMat)


def datingClassTest():
	hoRatio = 0.10
	# datingDataMat, datingLabels = file2Matrix('datingTestSet2.txt')
	# normMat, ranges, minVals = autoNorm(datingDataMat)
	m = normMat.shape[0]
	numTestVecs = int(m*hoRatio)
	errorCount = 0.0
	for i in range(numTestVecs):
		classifierResult = classify0(normMat[i, :], normMat[numTestVecs:m, :], datingLabels[numTestVecs:m], 3)
		# print("계산 값 - %d   실제 값- %d" % (classifierResult, datingLabels[i]))
		if (classifierResult != datingLabels[i]):
			errorCount += 1.0
	print("error count %f" % (errorCount / float(numTestVecs)))


def classifyPerson():
	resultList = ['별로임', '살짝...?', '개좋아']
	percentTats = float(input("비디오 게임 얼마나 하니?"))
	ffMiles = float(input("1년에 비행기 어느정도 타?"))
	iceCream = float(input("1년에 아이스크림을 몇리터나 먹어?"))
	inArr = array([ffMiles, percentTats, iceCream])
	classifierResult = classify0((inArr - minVals)/ranges, normMat, datingLabels, 3)

	print("넌 아마 이 사람을...", resultList[int(classifierResult) - 1])

datingDataMat, datingLabels = file2Matrix('datingTestSet2.txt')
normMat, ranges, minVals = autoNorm(datingDataMat)



datingClassTest()
classifyPerson()
print(datingDataMat)
print(autoNorm(datingDataMat))
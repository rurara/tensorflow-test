from math import log
import matplotlib
import matplotlib.pyplot as plt

def calcShannonEnt(dataSet):
	numEntries = len(dataSet)
	labelCounts = {}
	for featVec in dataSet:
		currentLabel = featVec[-1]
		if currentLabel not in labelCounts.keys():
			labelCounts[currentLabel] = 0
		labelCounts[currentLabel] += 1
	calcShannonEnt = 0.0
	for key in labelCounts:
		prob = float(labelCounts[key] / numEntries)
		calcShannonEnt -= prob * log(prob, 2)
	return calcShannonEnt

def createDataSet():
	returnDataSet = [
		[1,1,'yes'],
		[1,1,'yes'],
		[1,0,'no'],
		[0,1,'no'],
		[0,1,'no'],
	]
	labels = ['no surfacing', 'flippers']

	return returnDataSet, labels

def splitDataSet(dataSet, axis, value):
	retDataSet = []
	for featVec in dataSet:
		if featVec[axis] == value:
			reducedFeatVec = featVec[:axis]
			reducedFeatVec.extend(featVec[axis+1:])
			retDataSet.append(reducedFeatVec)
	return retDataSet


def chooseBestFeatureToSplit(dataSet):
	numFeatures= len(dataSet[0]) - 1
	baseEntropy = calcShannonEnt(dataSet)
	bestInfoGain = 0.0; bestFeature = -1

	for i in range(numFeatures):
		featList = [example[i] for example in dataSet]
		uniqueVals = set(featList)
		newEntropy = 0.0
		for value in uniqueVals:
			subDataSet = splitDataSet(dataSet, i, value)
			prob = len(subDataSet) / float(len(dataSet))
			newEntropy += prob * calcShannonEnt(subDataSet)
		infoGain = baseEntropy - newEntropy
		if (infoGain > bestInfoGain):
			bestInfoGain = infoGain
			bestFeature = i
	return bestFeature

def createTree(dataSet, labels):
	classList = [example[-1] for example in dataSet]
	if classList.count(classList[0]) == len(classList):
		return classList[0]
	if len(dataSet[0]) == 1:
		return majorityCnt(classList)
	bestFeat = chooseBestFeatureToSplit(dataSet)
	bestFeatLabel = labels[bestFeat]
	myTree = {bestFeatLabel:{}}
	del(labels[bestFeat])
	featValues = [example[bestFeat] for example in dataSet]
	uniqueVals = set(featValues)
	for value in uniqueVals:
		subLabels = labels[:]
		myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet, bestFeat, value), subLabels)
	return myTree	


#챠트
decisionNode = dict(boxstyle="sawtooth",fc="0.8")
leafNode = dict(boxstyle="round4", fc="0.8")
arrow_args = dict(arrowstyle="<-")

def plotNode(nodeText,centerPt, parentPt, nodeType):
	createPlot.ax1.annotate(nodeText, xy=parentPt,xycoords="axex fraction", xytext=centerPt, textcoords="axes fraction", va="center", ha="center", bbox=nodeType, arrowprops=arrow_args)

def createPlot():
	fig = plt.figure(1, facecolor='white')	
	fig.clf()
	createPlot.ax1 = plt.subplot(111, frameon=False)
	plotNode('a decision node', (0.5, 0.1), (0.1, 0.5), decisionNode)
	plotNode('a decision node', (0.8, 0.1), (0.3, 0.8), leafNode)
	plt.show()



tempDataSet, labels = createDataSet()


createPlot()

splitDataSet(tempDataSet, 0, 0)

data = calcShannonEnt(tempDataSet)
myTree = createTree(tempDataSet, labels)
print(tempDataSet)
print(myTree)
print(data)
print(chooseBestFeatureToSplit(tempDataSet))

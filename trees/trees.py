from math import log

def clacShannonEnt(dataSet):
	numEntries = len(dataSet)
	labelCounts = {}
	for featVec in dataSet:
		currentLabel = featVec[-1]
		if currentLabel not in labelCounts.keys():
			labelCounts[currentLabel] = 0
		labelCounts[currentLabel] += 1
	clacShannonEnt = 0.0
	for key in labelCounts:
		prob = float(labelCounts[key] / numEntries)
		clacShannonEnt -= prob * log(prob, 2)
	return clacShannonEnt

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

tempDataSet, labels = createDataSet()


data = clacShannonEnt(tempDataSet)
print(data)
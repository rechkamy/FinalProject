from __future__ import division
import os
import sys
import operator
import math

def trainRocchio(foreground):
  dominanceVec = []
	for value in foreground:
		if value[1] >= 25:
			category = value[0]
			foregroundCoverage = value[1]/fLength
			for item in background:
				if item[0] == category:
					backgroundCoverage = item[1]/bLength
					break

			dominance = foregroundCoverage/backgroundCoverage
			dominanceVec.append((category, dominance))

	dominanceVec.sort(key=operator.itemgetter(1), reverse=True)
	for i in range(10):
		try:
			file.write(description + ' ' + dominanceVec[i][0] + ' ' + str(dominanceVec[i][1]) + '\n')
		except:
			break

  
def testRocchio(description, dictionary):
  file.write(description + '\n')
	for value in dictionary[:100]:
		file.write(value[0] + '\t' + str(round(value[1]/len(dictionary), 3)) + '\n')
	file.write('\n')
  
  

def main():
  filename = argv[1]
  tweets = open(filename, 'r').read().split('\n')
  length = len(tweets)
  
  trainLength = floor(length*0.8)
  testLength = length - trainLength
  
  training = tweets[:trainLength]
  testing = tweets[trainLength:]
  

if __name__ == '__main__':
    main()
from __future__ import division
import os
import sys
import operator
import math

def trainRocchio:

  
def testRocchio:
  
  

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
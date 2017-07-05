from __future__ import print_function
import numpy as np
import sys
import os
import string
import itertools
from pprint import pprint
from random import shuffle

encodingDict = {
  '0': [0, 0, 0],
  '+': [1, 0, 0],
  '-': [0, 1, 0],
  'I': [0, 0, 1]
}

def getSequences(sequence_length = 5):
  inputData = []
  outputData = []

  decodedSequences = list(itertools.product(encodingDict.keys(), repeat = sequence_length))
  shuffle(decodedSequences)

  for decodedSequence in decodedSequences:
    inputData.append(encodeSequence(decodedSequence))

    outputData.append(calculateOutput(decodedSequence))

  return [inputData, outputData]

def encodeSequence(sequence):
    sequenceList = [encodingDict[char] for char in sequence]
    return np.array(sequenceList)

def calculateOutput(sequence):
    sum = 0
    inverse = 1
    for char in sequence:
      if char == '+':
        sum += 1 * inverse
      elif char == '-':
        sum -= 1 * inverse
      elif char == 'R':
        sum = 0
      elif char == 'I':
        inverse *= -1
    return sum

    maxSequenceLength = len(sequence) * 2

    out_list = ([0] * (maxSequenceLength + 1))
    out_list[sum + maxSequenceLength / 2] = 1
    return out_list

def decodeSequence(encodedSequenceArray):
  return string.join([[char for char, encoding in encodingDict.iteritems() if list(i) == encoding][0] for i in encodedSequenceArray], "")

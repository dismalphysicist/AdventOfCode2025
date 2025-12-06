#!/usr/bin/env python3
import numpy as np

input = []
operations = []
with open("input6.txt","r") as f:
  input = f.read().strip().split("\n")
  for i in range(len(input)):
    input[i] = input[i].split() # split by any whitespace
    if i==len(input)-1:
      # row of operations
      operations = input[i]
      input.pop()

transposed = np.transpose(np.array(input,dtype=int))

# part 1: grand total is sum of answers to all problems
totalp1 = 0
for i,op in enumerate(operations):
  if op=="+":
    totalp1 += np.sum(transposed[i])
  elif op=="*":
    totalp1 += np.prod(transposed[i])
  else:
    print("Error, unrecognised operation")

print("Part 1: grand total =",totalp1)
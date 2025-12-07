#!/usr/bin/env python3
import numpy as np

def mysum(lst):
  res = ""
  for n in lst:
    if n==" ":
      continue
    res += n
  if len(res)!= 0:
    return int(res)
  else:
    return 0

def condense(lst,numsums):
  res = [[0]]*numsums
  i = 0
  for lsti in range(len(lst)):
    sum = mysum(lst[lsti])
    if sum!=0:
      if res[i]==[0]:
        res[i] = [sum]
      else:
        res[i].append(sum)
    else:
      i += 1
  return res

input = []
input2 = []
operations = []
numlines = 0

with open("input6.txt","r") as f:
  input = f.read().strip().split("\n")

input2 = input.copy()

numlines = len(input)-1 # subtract one for row of operations
for i in range(len(input)):
  if i==len(input)-1:
    # row of operations
    operations = input[i].split()
    input.pop()
    input2.pop()
  else:
    input[i] = input[i].split() # split by any whitespace
    input2[i] = [c for c in input2[i]] # split every character including spaces

# part 1: grand total is sum of answers to all problems
transposed = np.transpose(np.array(input,dtype=int))
# part 2: read numbers vertically, same problem as part 1
transposed2 = np.transpose(np.array(input2)) # still includes spaces
condensed = condense(transposed2,len(transposed))

def calculate(nums,ops):
  res = 0
  for i,op in enumerate(ops):
    if op=="+":
      res += np.sum(nums[i])
    elif op=="*":
      res += np.prod(nums[i])
    else:
      print("Error, unrecognised operation")
  return res

totalp1 = calculate(transposed,operations)
totalp2 = calculate(condensed,operations)

print("Part 1: grand total =",totalp1)
print("Part 2: grand total =",totalp2)
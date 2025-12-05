#!/usr/bin/env python3

def inRange(num,rg): # inclusive of endpoints
  if num>=rg[0] and num<=rg[1]:
    return True
  else:
    return False

def condensable(range1,range2):
  if inRange(range1[0],range2) or inRange(range1[1],range2) or inRange(range2[0],range1) or inRange(range2[1],range1):
    return True
  else:
    return False

def newEndpoints(range1,range2):
  # assumes range1 and range2 are condensable
  # assumes endpoints are integers
  return [min(range1[0],range2[0]),max(range1[1],range2[1])]

##########################################################################

ranges = []
ids = []
# parse input, read everything as integers
with open("input5.txt","r") as f:
  ranges, ids = f.read().strip().split("\n\n")
  ranges = ranges.split("\n")
  for i in range(len(ranges)):
    ranges[i] = [int(n) for n in ranges[i].split("-")]
  ids = [int(id) for id in ids.split("\n")]

# part 1: find how many ids are in the fresh ranges
totalp1 = 0
for id in ids:
  for rg in ranges:
    if inRange(id,rg):
      totalp1 += 1
      break # don't need to keep checking ranges

# part 2: how many fresh ingredients total, disregarding available ids
# (a set works but is too memory-intensive)

# clean up ranges
for i in range(len(ranges)):
  if len(ranges[i])!=2:
      continue
  while(True):
    changed = False
    for j in range(i+1,len(ranges)):
      if len(ranges[i])!=2 or len(ranges[j])!=2:
        continue
      if condensable(ranges[i],ranges[j]):
        ranges[i] = newEndpoints(ranges[i],ranges[j])
        ranges[j] = [] # don't mess up indexing
        changed = True
    if not changed:
      break

# naive sum works now
totalp2 = 0
for rg in ranges:
  if len(rg)==2: # skip empty ones
    totalp2 += rg[1]-rg[0]+1 # inclusive!

print("Part 1: total number of fresh available ingredients =",totalp1)
print("Part 2: total number of fresh ingredients =",totalp2)
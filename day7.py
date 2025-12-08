#!/usr/bin/env python3

input = []
with open("input7.txt","r") as f:
  input = f.read().strip().split("\n")
  for i in range(len(input)):
    input[i] = [c for c in input[i]] # now we have a 2D list

# tachyon enters at S
def start(map,questionPart):
  for j in range(len(map[0])):
    if map[0][j]=="S":
      if questionPart==1:
        map[0][j] = "|"
      else:
        map[0][j] = "1" # counting timelines
      return

# propagates downwards unless it meets a splitter
def propagate1step(map,i):
  count = 0
  # i is the line we are currently on
  for j in range(len(map[i])):
    if map[i][j]=="|":
      # either there is a splitter below
      if map[i+1][j]=="^":
        count += 1
        try:
          # splitters are never adjacent so no need to worry about overwriting a splitter
          map[i+1][j-1] = "|"
          map[i+1][j+1] = "|"
        except IndexError:
          print("Beam propagating off edge of map")
      # or not, and we propagate downwards
      else:
        map[i+1][j] = "|"
  return count

def fill(sink,source):
  if sink!=".":
    sink = str(int(sink)+int(source))
  else:
    sink = source
  return sink

def propagatePart2(map,i):
  # i is the line we are currently on
  for j in range(len(map[i])):
    # tachyon is represented by a digit
    # the digit is the number of timelines that lead there
    if map[i][j]!="." and map[i][j]!="^":
      # either there is a splitter below
      if map[i+1][j]=="^":
        try:
          # splitters are never adjacent so no need to worry about overwriting a splitter
          map[i+1][j-1] = fill(map[i+1][j-1],map[i][j])
          map[i+1][j+1] = fill(map[i+1][j+1],map[i][j])
        except IndexError:
          print("Beam propagating off edge of map")
      # or not, and we propagate downwards
      else:
        # still need to be careful of merging timelines
        map[i+1][j] = fill(map[i+1][j],map[i][j])

# iterate downwards through the map, modifying as we go
def propagate(map):
  start(map,1)
  count = 0
  for i in range(len(map)-1):
    count += propagate1step(map,i)
  return count

def countTimelines(map):
  start(map,2)
  timelines = 0
  for i in range(len(map)-1):
    propagatePart2(map,i)
  # count timelines
  for j in range(len(map[-1])):
    if map[-1][j]!=".":
      timelines += int(map[-1][j])
  return timelines

inputp1 = [input[i].copy() for i in range(len(input))]
totalp1 = propagate(inputp1)
totalp2 = countTimelines(input)

print("Part 1: how many times does beam split?",totalp1)
print("Part 1: how many timelines are created?",totalp2)
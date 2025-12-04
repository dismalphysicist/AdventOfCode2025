#!/usr/bin/env/python3

# input parsing
input = []
with open("input4.txt","r") as f:
  input = f.read().strip().split("\n")
for i in range(len(input)):
  input[i] = [c for c in input[i]]
numrows = len(input)
numcols = len(input[0])

# define useful functions
def onCorner(row,col):
  if int(row==0)+int(col==0)+int(row==numrows-1)+int(col==numcols-1) == 2:
    return True
  else:
    return False

def onEdge(row,col):
  if row==0 or col==0 or row==numrows-1 or col==numcols-1:
    return True
  else:
    return False

def numRollsOnEdge(map,row,col):
  # more careful version of numRolls
  if row==0:
    return  int(map[row][col-1]=="@")   \
          + int(map[row][col+1]=="@")   \
          + int(map[row+1][col-1]=="@") \
          + int(map[row+1][col]=="@")   \
          + int(map[row+1][col+1]=="@")
  elif row==numrows-1:
    return  int(map[row-1][col-1]=="@") \
          + int(map[row-1][col]=="@")   \
          + int(map[row-1][col+1]=="@") \
          + int(map[row][col-1]=="@")   \
          + int(map[row][col+1]=="@")
  elif col==0:
    return  int(map[row-1][col]=="@")   \
          + int(map[row-1][col+1]=="@") \
          + int(map[row][col+1]=="@")   \
          + int(map[row+1][col]=="@")   \
          + int(map[row+1][col+1]=="@")
  elif col==numcols-1:
    return  int(map[row-1][col-1]=="@") \
          + int(map[row-1][col]=="@")   \
          + int(map[row][col-1]=="@")   \
          + int(map[row+1][col-1]=="@") \
          + int(map[row+1][col]=="@")

def numRolls(map,row,col):
  if onCorner(row,col):
    return 3 # max
  if onEdge(row,col):
    return numRollsOnEdge(map,row,col)
  else:
    return  int(map[row-1][col-1]=="@") \
          + int(map[row-1][col]=="@")   \
          + int(map[row-1][col+1]=="@") \
          + int(map[row][col-1]=="@")   \
          + int(map[row][col+1]=="@")   \
          + int(map[row+1][col-1]=="@") \
          + int(map[row+1][col]=="@")   \
          + int(map[row+1][col+1]=="@")

def updateMap(map,positions):
  for (i,j) in positions:
    if map[i][j] == "@":
      map[i][j] = "."
    else:
      print("Error, no paper roll in position",(i,j))

# part 1: how many rolls of paper can we access straight away?
canAccess = 0

for i in range(numrows):
  for j in range(numcols):
    if input[i][j] == "@":
      if numRolls(input,i,j) < 4:
        canAccess += 1

print("Part 1: how many rolls can be accessed now?", canAccess)

# part 2: what if we repeat that process?
totalp2 = 0
foundPositions = []
lastNumRemoved = 1 # init value, must be non-zero since python has no do-while
while lastNumRemoved > 0:
  lastNumRemoved = 0
  for i in range(numrows):
    for j in range(numcols):
      if input[i][j] == "@":
        if numRolls(input,i,j) < 4:
          lastNumRemoved += 1
          totalp2 += 1
          foundPositions.append((i,j))
  updateMap(input,foundPositions)
  foundPositions = []

print("Part 2: how many rolls can be accessed eventually?", totalp2)
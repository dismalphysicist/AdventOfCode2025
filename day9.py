#!/usr/bin/env python3
from matplotlib import pyplot as plt

input = []
with open("input9.txt","r") as f:
  input = f.read().strip().split("\n")
  for i in range(len(input)):
    input[i] = [int(n) for n in input[i].split(",")]

# part 1: find the largest area of any rectangle
def area(p1,p2):
  return (abs(p2[0]-p1[0])+1)*(abs(p2[1]-p1[1])+1)

# part 2: make sure it only contains red and green tiles

def horizontal(p1,p2):
  if p1[0]==p2[0]:
    return True
  else:
    return False

def length(line):
  # shortcut for purely vertical or purely horizontal lines
  return max(abs(line[0][0]-line[1][0]),abs(line[0][1]-line[1][1]))

def constructVertices(p1,p2):
  topleft = [min(p1[0],p2[0]),min(p1[1],p2[1])]
  topright = [topleft[0],max(p1[1],p2[1])]
  bottomleft = [max(p1[0],p2[0]),topleft[1]]
  bottomright = [bottomleft[0],topright[1]]
  # return as if drawn clockwise
  return [topleft,topright,bottomright,bottomleft]

def redgreenCorners(rect,lst):
  for corner in rect:
    red = False
    if corner in lst:
      red = True
    if not red:
      # check if green
      if not isGreen(corner,lst):
        return False
  return True

def redgreenCentre(rect,lst):
  centre = [(rect[0][0]+rect[3][0])//2,(rect[0][1]+rect[1][1])//2]
  if isGreen(centre,lst):
    return True
  else:
    return False

def findEdges(pos,pair,edges):
  if horizontal(pair[0],pair[1]):
    # edge is north of pos if 0th coord is <= than pos's
    # and pos's 1st coord is in the range spanned by the edge
    if pos[1]>=min(pair[0][1],pair[1][1]) and pos[1]<=max(pair[0][1],pair[1][1]):
      if pos[0]>=pair[0][0]:
        edges[0] = True
      if pos[0]<=pair[0][0]:
        edges[1] = True
  else:
    # vertical. Edge is east of pos if 1st (2nd) coord is >= than pos's
    if pos[0]>=min(pair[0][0],pair[1][0]) and pos[0]<=max(pair[0][0],pair[1][0]):
      if pos[1]<=pair[0][1]:
        edges[2] = True
      if pos[1]>=pair[0][1]:
        edges[3] = True
  return edges

def isGreen(pos,lst):
  # tile is green if it is physically between two adjacent points in lst
  # including wrapping: between last and first
  # and the entire area contained in this is green
  # tile is green if it is all of: to the left of an edge and to the right
  # and to the north and to the south of an edge
  edges = [False,False,False,False] # N,S,E,W
  for i in range(len(lst)-1):
    edges = findEdges(pos,[lst[i],lst[i+1]],edges)
  # handle wrapping
  edges = findEdges(pos,[lst[-1],lst[0]],edges)

  if edges==[True,True,True,True]:
    return True
  else:
    return False

def inside(rect,line):
  # find if any part of the line is completely inside the rectangle
  # i.e. not on the boundaries or outside
  if line[0][0] in range(rect[0][0]+1,rect[3][0]) and line[0][1] in range(rect[0][1]+1,rect[1][1]):
    return True
  if line[1][0] in range(rect[0][0]+1,rect[3][0]) and line[1][1] in range(rect[0][1]+1,rect[1][1]):
    return True
  if horizontal(line[0],line[1]):
    if line[0][1]<=rect[0][1] and line[1][1]>=rect[0][1] and line[0][0]>rect[0][0] and line[0][0]<rect[3][0]:
      return True
    if line[0][1]<=rect[1][1] and line[1][1]>=rect[1][1] and line[0][0]>rect[0][0] and line[0][0]<rect[3][0]:
      return True
  else:
    if line[0][0]<=rect[0][0] and line[1][0]>=rect[0][0] and line[0][1]>rect[0][1] and line[0][1]<rect[1][1]:
      return True
    if line[0][0]<=rect[3][0] and line[1][0]>=rect[3][0] and line[0][1]>rect[0][1] and line[0][1]<rect[1][1]:
      return True

def anyInside(rect,shape):
  for i in range(len(shape)-1):
    if length([shape[i],shape[i+1]])>1: # lines of length 1 cannot affect anything
      if inside(rect,[shape[i],shape[i+1]]):
        return True
  if inside(rect,[shape[-1],shape[0]]):
    return True
  else:
    return False

largestArea = 1
largestp2 = 1
for i1 in range(len(input)):
  for i2 in range(i1+1,len(input)):
    A = area(input[i1],input[i2])
    if A > largestArea:
      largestArea = A
    # part 2
    if A > largestp2:
      # check whether the edges of the rectangle cross any of the edges in the input
      # if so, then one side or the other must not be green
      # catch: must also check the rectangle corners are actually green
      rectCorners = constructVertices(input[i1],input[i2])
      if redgreenCorners(rectCorners,input):
        # check we are not in a hole in the shape
        # by explicitly checking the centre point
        if redgreenCentre(rectCorners,input):
          if not anyInside(rectCorners,input):
            finalRect = rectCorners.copy()
            largestp2 = A

print("Part 1: largest rectangle has area",largestArea)
print("Part 2: largest rectangle containing only red/green tiles has area",largestp2)

xs,ys = zip(*input)
plt.figure()
plt.plot(ys,xs)
rxs,rys = zip(*finalRect)
plt.plot(rys,rxs)
plt.savefig("day9-final.png")
plt.show()
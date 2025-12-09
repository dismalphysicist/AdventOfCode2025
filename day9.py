#!/usr/bin/env python3

input = []
with open("input9.txt","r") as f:
  input = f.read().strip().split("\n")
  for i in range(len(input)):
    input[i] = [int(n) for n in input[i].split(",")]

# part 1: find the largest area of any rectangle
def area(p1,p2):
  return (abs(p2[0]-p1[0])+1)*(abs(p2[1]-p1[1])+1)

largestArea = 1
for i1 in range(len(input)):
  for i2 in range(i1+1,len(input)):
    A = area(input[i1],input[i2])
    if A > largestArea:
      largestArea = A

print("Part 1: largest rectangle has area",largestArea)
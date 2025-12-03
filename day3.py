#!/usr/bin/env python3

input = []
with open("input3.txt","r") as f:
  input = f.read().strip().split("\n")

def findMaxN(lst,n):
  res = ""
  startpos = 0
  endpos = -n+1
  for _ in range(n):
    battery = max(lst[startpos:endpos])
    res += str(battery)
    startpos = startpos+lst[startpos:endpos].index(battery)+1
    endpos += 1
    if (endpos==0):
      endpos = len(lst)+1
  return int(res)

totalp1 = 0
totalp2 = 0
# turn into list of lists of single-digit integers
# part 1: find biggest output from 2 of the digits, read as 2-digit number in order
for i in range(len(input)):
  input[i] = [int(n) for n in input[i]]

  # initial solve of part 1:
  # line = input[i]
  # battery1 = max(line[:-1])
  # battery2 = max(line[line.index(battery1)+1:])
  # totalp1 += int(str(battery1)+str(battery2))

  totalp1 += findMaxN(input[i],2)
  totalp2 += findMaxN(input[i],12)

print("Part 1: maximum possible joltage with 2 batteries =",totalp1)
print("Part 2: maximum possible joltage with 12 batteries =",totalp2)

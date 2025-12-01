#!/usr/bin/env python3

input = []
with open("input1.txt","r") as f:
  input = f.read().strip().split("\n")

# part 1: count how many times the dial points at 0 after each instruction
# part 2: count how many times the dial passes through 0
pwd1 = 0
pwd2 = 0
total = 50
for l in input:
  clicks = int(l[1:])
  add = True

  if l[0]=="L": # anticlockwise
    sign = -1
    pos = 100-total
    if total==0:
      add = False

  else: # going clockwise
    sign = 1
    pos = total
  
  pwd2 += clicks//100
  if add: # prevent double counting
    pwd2 += abs((pos+clicks%100)//100)

  total += sign*clicks
  total = total%100
  
  if total==0:
    pwd1 += 1

print("Part 1: password is",pwd1)
print("Part 2: password is",pwd2)
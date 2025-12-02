#!/usr/bin/env python3
import re

def repeatingp1(nstring):
  for i in range(len(nstring)):
    if nstring[0:i] == nstring[i:]:
      return True
  return False

def repeatingp2(nstring):
  # do not try and use {2,} for this, it does not work
  atleast2 = re.compile(r'^([0-9]+)\1+$')
  m = re.match(atleast2,nstring)
  if m and m.start()==0 and m.end()==len(nstring):
    return True
  return False

ranges = []
with open("input2.txt","r") as f:
  ranges = [(int(rg.split("-")[0]), int(rg.split("-")[1])) for rg in f.read().strip().split(",")]

invalidp1 = 0
invalidp2 = 0

for (start,end) in ranges:
  for n in range(start,end+1):
    if repeatingp1(str(n)):
      invalidp1 += n
    if repeatingp2(str(n)):
      invalidp2 += n

print("Part 1: sum of all invalid IDs =", invalidp1)
print("Part 2: sum of all invalid IDs =", invalidp2)

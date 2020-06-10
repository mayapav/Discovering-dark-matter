import math
import numpy as np 

file=open('Galaxy1 (4).txt','r')
file.readline

radius=[]
Mc=[]
p0=100*(10**6)
rc=1.87

for line in file:
  radius.append(float(line.split('\t')[0]))

u= 4*(math.pi)*(p0)*(rc**2) 


for i in radius:
  k=math.atan(i/rc)
  j=i-(rc*k)
#Mc_results=
#ApproxPi.py
#Name:
#Date:
#Assignment:
import math
import time


#PLEASE NOTE - This is an optional, extra credit portion of the lab.

def main():
  realPi = math.pi

  #ask user for decimal percision (up to 10)

  approxPi = 4/1
sign = -1
denom = 3
for i in range(100):
  print(approxPi)
  
  start = time.time()
  while round(approxPi, 7)  != round(realPi, 7):
  #calculate pi using the approximation technique
  #Loop until the level of percision is reached
   
  
 #print(ApproxPi)
    approxPi = approxPi + sign * 4/denom 
  end = time.time()

  
  print(elapsedTime)

if __name__ == '__main__':
  main()

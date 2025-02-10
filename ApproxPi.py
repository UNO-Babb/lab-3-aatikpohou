#ApproxPi.py
#Name:
#Date:
#Assignment:
import math
import time


#PLEASE NOTE - This is an optional, extra credit portion of the lab.
def main():3

realPi = math.pi
  #ask user for decimal percision (up to 10)
decimal_precision = int(input("how many decinal points to compute (0-10): "))
#print = decimal_precision
start = time.time()
  #calculate pi using the approximation technique
  #Loop until the level of percision is reached
approxPi = 4/1
sign = -1
denom = 3
while round(approxPi, decimal_precision)  != round(realPi, decimal_precision):   
  #print(ApproxPi)
  approxPi = approxPi + sign * 4/denom 
  sign = sign * - 1
  denom = denom + 2
end = time.time()
elapsedTime = end - start
#print(elapsedTime)
print(elapsedTime)
if __name__ == '__main__':
    main()

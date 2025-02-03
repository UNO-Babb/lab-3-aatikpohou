#TempConvert.py
#Name:
#Date:
#Assignment:


def main():
  #Prompt the user for a Fahrenheit temperature
  #Convert that temperature to celsius, rounding to 1 decimal percision
  #Output converted temperature.
  tempF = input ("Enter temperature")

  tempC =  int(tempF) - 32 
  tempC1 = (tempC) * 5/9 
  tempC = int(tempC1)

  print(tempF, "is ", tempC, "degrees celsius.")
if __name__ == '__main__':
  main()

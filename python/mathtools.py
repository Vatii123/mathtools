# author : piyaphatliamwilai (https://github.com/piyaphatliamwilai/mathtools & https://github.com/piyaphatliamwilai/somethingg), vatii123 (implements somethingg)

import time

print("4 in 1 Math Solution by https://github.com/piyaphatliamwilai & Vatii123 https://github.com/vatii123 :)")

firstNumber = float(input("Give first number (preferably highest number) -> "))
secondNumber = float(input("Give second number (preferably lowest number) -> "))

# subtraction
subtractAnswer = firstNumber - secondNumber;
print("-------- Subtraction --------")
print(subtractAnswer)
# multiplication
multiplyAnswer = firstNumber * secondNumber;
print("-------- Multiplication --------")
print(multiplyAnswer)
# division
divideNumber = firstNumber / secondNumber;
print("-------- Division --------")
print(divideNumber)
# exponent
exponentNumber = firstNumber ** secondNumber;
print("-------- Exponent --------")
print(exponentNumber)
# somethingg
divider = 1
print("-------- Factor (1) --------")
while 3 > 2:
    outputCalculate = firstNumber
    outputCalculate = outputCalculate / divider
    numberChecker = (outputCalculate.is_integer())
    if (numberChecker == True):
        print(outputCalculate)
    elif (numberChecker == False):
        time.sleep(0.000000001)
    divider = divider + 1
# check divideNumber
if (divider == firstNumber):
  print("finished checking first factor (1) continuing factor 2")
divider = 1
while 3 > 2:
    time.sleep(1)

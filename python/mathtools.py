import time

print("4 in 1 Math Solution by https://github.com/piyaphatliamwilai :)")

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

while 3 > 2:
    time.sleep(1)

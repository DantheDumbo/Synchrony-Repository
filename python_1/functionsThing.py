def addNumbers(firstNumber, secondNumber):
   sum = firstNumber + secondNumber
   print("The sum is", str(sum), ".")


def subtractNumbers(firstNumber, secondNumber):
   difference = firstNumber - secondNumber
   print("The difference is", str(difference), ".")


def multiplyNumbers(firstNumber, secondNumber):
   product = firstNumber * secondNumber
   print("The product is", str(product), ".")


def divideNumbers(firstNumber, secondNumber):
   if secondNumber == 0:
       print("Division by zero? Nah, that ain't gonna work!")
   else:
       quotient = firstNumber / secondNumber
       print("The quotient is", str(quotient), ".")


def numberAndExponent(firstNumber, secondNumber):
   num = pow(firstNumber, secondNumber)
   print("The result is", str(num), ".")


def main():  # Main program
   print("yo this my calc and I can do all this why dont you slide some numbers to compute")
   # Create a list of menu options
   menu_options = [
       "1. Addition",
       "2. Subtraction",
       "3. Multiplication",
       "4. Division",
       "5. Exponents"
   ]
  
   # Loop through and print each option
   for option in menu_options:
       print(option)
  
   try:
       userOption = int(input("Please just select something and dont take too long: "))


       if userOption not in [1, 2, 3, 4, 5]:
           print("Not a valid number bozo.")
           return


       firstNumber = float(input("You better give me the first number right now or else... "))
       secondNumber = float(input("Now the second... "))


       if userOption == 1:
           addNumbers(firstNumber, secondNumber)
       elif userOption == 2:
           subtractNumbers(firstNumber, secondNumber)
       elif userOption == 3:
           multiplyNumbers(firstNumber, secondNumber)
       elif userOption == 4:
           divideNumbers(firstNumber, secondNumber)
       elif userOption == 5:
           numberAndExponent(firstNumber, secondNumber)


   except ValueError:
       print("Bruh, that's not a number!")
      
main()
def calc(num1, num2, operator):
  if operator == "+":
    return num1 + num2
  elif operator == "-":
    return num1 - num2
  elif operator == "*":
    return num1 * num2
  elif operator == "/":
    return num1 / num2

num1 = int(input("Enter a number: "))
operator = input("Enter an operator: ")
num2 = int(input("Enter another number: "))
A = calc(num1, num2, operator)
print("The answer is",A)
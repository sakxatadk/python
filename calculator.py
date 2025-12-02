a = float(input("Enter the first number:"))
b = float(input("Enter the second number:"))   
print("Enter the operation you want to perform:")
print("+ for Addition")
print("- for Subtraction")
print("* for Multiplication")
print("/ for Division")
op = input("Enter the operation symbol:")
match op:
    case "+":
        print(f"The sum of {a} and {b} is {a+b}")
    case "-":
        print("The subtraction of ", a ," and ", b ," is ", a-b)   
    case "*":
        print("The multiplication of ", a ," and ", b ," is ", a*b)
    case "/":
        print("The division of " ,a ," and ", b, " is ", a/b)
    case _:
        print("Invalid operation")    
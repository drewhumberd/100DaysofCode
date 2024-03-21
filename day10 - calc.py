from supportfiles.art import calc_logo

# Calculator Functions

# Add
def add(n1, n2):
  """Adds two numbers"""
  return n1 + n2

# Subtract
def subtract(n1, n2):
  """Subtracts second number from first number"""
  return n1 - n2

# Multiply
def multiply(n1, n2):
  """Multiplies two numbers"""
  return n1 * n2

# Divide
def divide(n1, n2):
  """Divides first number by second number"""
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator():
  print(calc_logo)
  num1 = float(input("What's the first number?: "))
  should_continue = True
  while should_continue == True:
    for symbol in operations:
      print(symbol)
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
  
    if operation_symbol == "+" or operation_symbol == "-" or operation_symbol == "*" or operation_symbol == "/":
      calculation_function = operations[operation_symbol]
      answer = calculation_function(num1, num2)
    else:
      print("Invalid operation symbol")
  
    print(f"{num1} {operation_symbol} {num2} = {answer}")
  
    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation:") == "y":
      num1 = answer
    else:
      should_continue = False
      calculator()

calculator()
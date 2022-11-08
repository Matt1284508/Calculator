from logo import logo
#Add
def add (n1, n2):
    return n1 + n2
#Subtract
def subtract (n1, n2):
    return n1 - n2
#Multiply
def multiply (n1, n2):
    return n1 * n2
#Divide
def divide (n1, n2):
    return n1 / n2

operation = {
    "+": add, 
    "-": subtract, 
    "*": multiply, 
    "/": divide,
}

def calculator():
    print(logo)
    num_1 = float(input("What is the first number?: "))
    calc_continue = True

    while calc_continue:
            operation_symbol = input("Pick an operation ( + - * / ): ")
            num_2 = float(input("What is the next number?: "))

            calculation_function = operation[operation_symbol]
            answer = calculation_function(num_1, num_2)
            print(f"{num_1} {operation_symbol} {num_2} = {answer}")
            
            if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit.: ") == "y":
                num_1 = answer 
                calc_continue = True
            else: 
                calculator()
                
calculator()

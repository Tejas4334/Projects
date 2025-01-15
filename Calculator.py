from functools import reduce

from django.db.models.expressions import result


def operationAdd(operands):
    result = reduce(lambda x , y : x+y , operands)
    return result

def operationMul(operands):
    result = reduce(lambda x , y : x*y , operands)
    return result


def operationDiv(operands):
    result = reduce(lambda x , y : x/y , operands)
    return result

def operationSub(operands):
    result = reduce(lambda x , y : x-y , operands)
    return result

def operationMod(operands):
    result = reduce(lambda x , y : x%y , operands)
    return result



operandsStr = input("Enter the Operands to operate and make sure to separate the value by space :- ")

operandsList = operandsStr.split()

operands = [int(x) for x in operandsList]

operation = (input("Enter the operation to be performed \n (for now + , * , / , % , - ) :- "))

if(operation == "+"):
    print(f" Your Result is {operationAdd(operands)}")
elif(operation == "*"):
    print(f" Your Result is {operationMul(operands)}")
elif (operation == "/"):
    print(f" Your Result is {operationDiv(operands)}")
elif (operation == "%"):
    print(f" Your Result is {operationMod(operands)}")
elif (operation == "-"):
    print(f" Your Result is {operationSub(operands)}")
else:
    print("Invalid Operation")


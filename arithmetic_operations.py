def addition(a : int,b : int) -> int:
    return a + b

def subtraction(a:int , b:int) -> int:
    return a - b

def multiplication(a:int , b:int) -> int:
    return a * b

def division(a:int , b:int)-> int:
    if b == 0:
        raise ZeroDivisionError("You tried to divide by zero!")

    return a/b

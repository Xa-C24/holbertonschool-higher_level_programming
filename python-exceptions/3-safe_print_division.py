#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        calcul = a / b
        print("Result: {:.1f}".format(calcul))
        return calcul
    except:
        ZeroDivisionError
        print("Result: None")
        return None

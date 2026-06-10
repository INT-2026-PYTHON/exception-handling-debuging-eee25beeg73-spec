n1=input("enter the number 1:")
n2=input("enter the number 2:")
def safe_divide(num1,num2):
    try:
        result = float(num1) / float(num2)
        return ("ok", result)

    except ValueError:
        return ("error", "Invalid input: please enter numeric values.")

    except ZeroDivisionError:
        return ("error", "Cannot divide by zero.")

    except Exception as e:
        return ("error", f"Unexpected error: {e}")
o=safe_divide(n1,n2)
print(o)
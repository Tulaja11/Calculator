def evaluate_expression(expression):
    try:
        result = str(eval(expression))
        return result
    except ZeroDivisionError:
        return "Error: Division by Zero"
    except Exception:
        return "Error"

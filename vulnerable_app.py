# Intentionally vulnerable code for testing SonarCloud

def calculate(expr):
    # ❌ Dangerous: eval allows arbitrary code execution
    return eval(expr)

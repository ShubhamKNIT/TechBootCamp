# Python Higher-Order Functions Example
def divisor(x):
    def dividend(y):
        return y / x
    return dividend

divide = divisor(2)
result = divide(10)
print("Result of dividing 10 by 2 using higher-order function:", result)
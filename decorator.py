# This is an example for decorator. Decorator is a function that takes another function as an argument and returns a new function.

'''
Step1: test_decorator function runs and enters inside function.
Step2: Inside function runs the print Before run Statement
Step3: Value calls the product function.
Step4: Product function runs the print Add function ran with inputs Statement
Step5: Inside function runs the print After run Statement
Step6: Final Print Product of 40 and 20 is 800 run Statement

Output:
Inside function Before run
Add function ran with inputs 40 , 20
Inside function After run
Product of 40 and 20 is 800
'''


def test_decorator(fn):
    def inside_function(a,b):
        print("Inside function Before run ")
        value = fn(a,b)
        print("Inside function After run ")
        return value
    return inside_function

@test_decorator
def product(a,b):
    print("Add function ran with inputs" , a, str(','), b)
    return a*b

a = 40
b = 20

print("Product of {} and {} is {}".format(a,b,product(a,b)))



def hello(a, b):
    return a*b
def func(a, b, c):
    print(a+b)
    print(c(a, b))


func(3, 7, lambda a, b: a*b )


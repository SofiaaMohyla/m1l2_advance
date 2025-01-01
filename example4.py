def func(a, b,*args, **kwargs):
    print(kwargs)


res1 = func(1, 2, 5, 6, c=3, d=4)

print(res1)

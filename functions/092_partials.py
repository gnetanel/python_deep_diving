from functools import partial


def my_print(a, b, c):
    print(f"{a=},{b=},{c=}")


print("using direct call, basic example sending all parameters")
my_print(10, 20, 30)

print("using partial basic example")
my_func = partial(my_print, 100)
my_func(20, 30)

print("====== more complex example ====== ")


def my_second_func(p1, p2, *args, kw1, kw2, **kwargs):
    print(f"{p1=}, {p2=}, {args=}, {kw1=}, {kw2=}, {kwargs=}")


print("using direct call,complex example all parameters")
my_second_func(10, 20, 30, 40, kw1=100, kw2=200, x1=300, x2=400)
print("using partial, complex example ")
my_partial_func = partial(my_second_func, 100, kw1=1000)
my_partial_func(20, 30, 40, kw2=200, x1=300, x2=400)


import operator

print(dir(operator))

# Some basic examples
operator.add(1, 2)
operator.mul(2, 3)
operator.truediv(3, 2)
operator.floordiv(10, 3)
operator.lt(10, 3)
operator.is_(1, 1)
operator.is_not(1, 1)
operator.truth(0)

# more common example
from functools import reduce

dummy_list = [1, 2, 3, 4, 5]
# instead calling
print(reduce(lambda x, y: x * y, dummy_list))
# we can now call without lambda
print(reduce(operator.mul, dummy_list))

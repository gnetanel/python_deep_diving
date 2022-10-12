from functools import reduce

my_list = [1, 9, 12, 32, 19, 23]
# reducing by getting the maximal value in the list
result = reduce(lambda a, b: a if a > b else b, my_list)
print(result)

# Common built-in reduce functions: sum, max, min, any, all

# any - return true if any of the element is truthy, i,e logical or
# example:
list1 = [True, False, True]
list2 = [False, False, False]
result = any(list1)
print("any() result")
print(result)
result = any(list2)
print(result)

# all, return true if all element are True, i.e: logical and
result = all(list1)
print("all() result")
print(result)
result = all(list2)
print(result)

# using initializer for reduce
my_list = [1, 2, 3]
result = reduce(lambda a,b : a + b, my_list, 100)
# would be 106
print(result)

n = 20
print("calculating factorial of n (n!)")
result = reduce(lambda a, b: a * b, range(1, n+1))
print(f"{result=}")


import time


def multi(n: int):
    def internal(i: int) -> int:
        return n * i

    return internal


def shared_closure(n: int):
    def adder(i: int) -> int:
        return n * i

    def multiplier(i: int) -> int:
        return n * i

    return adder, multiplier


# doing similar things between closure and class
def timer_closure():
    initial_time = time.perf_counter()

    def poll():
        nonlocal initial_time
        return initial_time - time.perf_counter()

    return poll


my_global_start_counter = 100


def not_closure_counter():
    def internal_counter(n: int):
        global my_global_start_counter
        return my_global_start_counter + n

    return internal_counter


class TimerClass:
    initial_time = 0

    def __init__(self):
        self.initial_time = time.perf_counter()

    def __call__(self, *args, **kwargs):
        return self.initial_time - time.perf_counter()


if __name__ == '__main__':
    print("== Basic closure == ")
    f1 = multi(10)
    f2 = multi(20)
    print(f1(100))
    print(f2(100))

    print("== shared free var between closure == ")
    print("Free var of f1", f1.__code__.co_freevars, )
    print("closure of f1", f1.__closure__)

    print("Shared free var on two closure")
    f1, f2 = shared_closure(100)
    print("Free var of f1 and f2, ", f1.__code__.co_freevars, f1.__code__.co_freevars)
    print("closure f1 and f2", f1.__closure__, f2.__closure__)

    print("== timer with closure and class == ")
    print("with closure")
    f1 = timer_closure()
    time.sleep(1)
    time_pass = f1()
    print("time pass with closure is ", time_pass)

    print("---- with class")
    timer_class = TimerClass()
    time.sleep(1)
    time_pass = timer_class()
    print("time pass with class is ", time_pass)

    print("===========not closure...")
    f1 = not_closure_counter()
    print(f1(100))
    print(f1(100))
    print("Increasing global from outside...")
    my_global_start_counter = 1000
    print("and calling again...")
    print("as can see no closure or free var, but changing immutable object global in one place affect the none "
          "closure function")
    print(f1(100))
    print("Free var of f1", f1.__code__.co_freevars)
    print("closure f1 and f2", f1.__closure__)

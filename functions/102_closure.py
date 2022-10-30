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


if __name__ == '__main__':
    print("== Basic closure == ")
    f1 = multi(10)
    f2 = multi(20)
    print(f1(100))
    print(f2(100))

    print("== shared free var between closure == ")
    print("Free var of f1", f1.__code__.co_freevars,)
    print("closure of f1", f1.__closure__)

    print("Shared free var on two closure")
    f1, f2 = shared_closure(100)
    print("Free var of f1 and f2, ", f1.__code__.co_freevars, f1.__code__.co_freevars)
    print("closure f1 and f2", f1.__closure__, f2.__closure__)
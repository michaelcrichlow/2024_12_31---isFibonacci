def isFibonacci(n: int) -> bool:
    # guard clause
    if n == 1:
        return True

    # The Fibonacci sequence by definition is linearly dependant
    # so I don't know if there's a more efficient version than this.
    res = 1
    _add = 1
    temp = 0
    while res <= n:
        if res == n:
            return True
        temp = res
        res += _add
        _add = temp

    return False


def main() -> None:
    print(isFibonacci(13))
    print(isFibonacci(2))
    print(isFibonacci(7))
    print(isFibonacci(8))
    print(isFibonacci(1_324))
    for val in range(1_000):
        if isFibonacci(val):
            print(val, end=" ")


if __name__ == '__main__':
    main()

# isFibonacci(13) => true

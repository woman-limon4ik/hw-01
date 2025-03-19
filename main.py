print('Hellow, world!')


def fib(n):
    lst = [0, 1]
    print(1, 2, sep='\n')
    for i in range(2, n):
        fib_n = lst[i - 1] + lst[i - 2]
        print(fib_n)
        lst.append(fib_n)
    return lst[-1]
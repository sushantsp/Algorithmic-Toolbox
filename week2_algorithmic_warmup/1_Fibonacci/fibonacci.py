# Uses python3
def calc_fib(n):
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)
def cal_fib1(n):
    if n <= 1:
        return n
    else:
        fib = [0,1]
        for i in range(2,n+1):
            fib.append(fib[i-1]+fib[i-2])
        return fib[-1]


n = int(input())
print(calc_fib(n))

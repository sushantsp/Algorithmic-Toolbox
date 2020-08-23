# Uses python3
import sys

def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % 10
def get_fibonacci_last_digit_naive1(n):
    if n <= 1:
        return n
    else:
        fib = [0,1]
        for i in range(2,n+1):
            fib.append((fib[i-1]+fib[i-2])%10)
        return fib[-1]



if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    # print(cal_fib1(n), get_fibonacci_last_digit_naive(n),get_fibonacci_last_digit_naive1(n))
    print( get_fibonacci_last_digit_naive1(n))

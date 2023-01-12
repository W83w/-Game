import time
def fibo(n):
    fib1 = 1
    fib2 = 1
    i = 0
    while i < n - 2:
        fib_sum = fib1 + fib2
        fib1 = fib2
        fib2 = fib_sum
        i = i + 1
    return fib2
def main():
    """Печать 1000 элемента последовательности Фибоначчи"""
    tic = time.perf_counter()
    result = fibo(1000)
    toc = time.perf_counter()
    print(f"Вычисление заняло {toc - tic:0.4f} секунд")
    print(result)
if __name__ == "__main__":
    main()


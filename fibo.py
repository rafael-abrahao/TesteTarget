def fibo(n: int) -> None:
    seq_fib = [0, 1]
    index = 1
    while seq_fib[-1] < n:
        next_num = seq_fib[-1] + seq_fib[-2]
        if next_num == n:
            print(f"O numero {n} pertence a sequencia de Fibonacci")
            return
        seq_fib.append(next_num)
    print(f"O numero {n} NAO pertence a sequencia de Fibonacci")
    
    
def main():
    try:
        n = input("Digite um numero: ")
        fibo(int(n))
    except ValueError:
        print("Digite apenas números inteiros")
    
if __name__ == "__main__":
    main()
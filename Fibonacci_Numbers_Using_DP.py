def fibonacci(n):
    if memo[n] != -1:
        return memo[n]
    else:
        if n == 1 or n == 2:
            result = 1
        
        else:
            result = fibonacci(n - 1) + fibonacci(n - 2)
        memo[n] = result
        return result
        
n = int(input())
memo = (n + 1) * [-1]
print(fibonacci(n))

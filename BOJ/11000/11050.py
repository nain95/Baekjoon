def factorial(n):
    ans = 1
    for i in range(2, n+1):
        ans *= i
    return ans
n,r = map(int,input().split())
print(factorial(n) // factorial(r) // factorial(n-r))
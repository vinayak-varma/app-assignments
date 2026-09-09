n=int(input("Enter the value of N:"))
dp=[0]*(n + 1) if n>=1 else [0]
if n>=1:
    dp[0]=0
if n>=2:
    dp[1]=1 
for i in range(2,n+1):
    dp[i]=dp[i-1]+dp[i-2]
print(f"\nFibonacci sequence up to {n} terms:")
for i in range(n):
    print(dp[i])
print()
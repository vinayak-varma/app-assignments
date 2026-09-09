n=int(input("Enter the number of houses:"))
houses=[]
print(f"Enter the amount present in each of the {n} houses:")
for i in range(n):
    amount=int(input(f"House {i+1}:"))
    houses.append(amount)
dp=[0]*(n+1)
if n>=1:
    dp[1]=houses[0]
for i in range(2,n+1):
    dp[i]=max(dp[i-1],houses[i-1]+dp[i-2])
print(f"\nHouse amounts: {houses}")
print(f"Maximum amount that can be collected: {dp[n]}")
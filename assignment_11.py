import pandas as pd

marks=[70,80,90]
s=pd.Series(marks)
m=pd.Series([1,2,3],index=["Amit","Sneha","Rahul"])
print(m)
print("Filtered:",s[s>70])
print("Mean:",s.mean())
print("Median:",s.median())
print("Minimum:",s.min())
print("Maximum:",s.max())

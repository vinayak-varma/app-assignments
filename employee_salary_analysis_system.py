import numpy as np
import pandas as pd

name=['Vinayak','Piyush','Yug','Paree','Shaan']
salary=[45000, 75000,55000,90000,65000]
arr=np.array(salary)
print("Average Salary:", np.mean(arr))
print("Maximum Salary:", np.max(arr))
print("Minimum Salary:", np.min(arr))
df=pd.DataFrame(
    {
    'Name': name,
    'Salary': salary
})
print("\nEmployee Data:")
print(df)
print("\nEmployees earning more than 60000:")
print(df[df['Salary']>60000])
import numpy as np
import pandas as pd

book=['Python','Java','C Programming','DBMS','AI']
price=[450,600,350,550,800]
arr=np.array(price)
print("Average Book Price:", np.mean(arr))
df=pd.DataFrame(
    {
    'Book': book,
    'Price': price
})
print("\nBook Details:")
print(df)
print("\nBooks costing more than 500:")
print(df[df['Price']>500])
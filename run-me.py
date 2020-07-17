import pyodbc 
import pandas as pd
from pandas import DataFrame
import pandas.io.sql as psql




df = pd.read_excel('list-sql.xlsx')  
df = df['Target-Convert']
df=df.tolist()

b=''
a=''
count=0

for i in df:
    
    if i == df[0]:
        b = "("+"'"+str(i)+"'"+","
    elif i == df[-1]:
        b = "'"+str(i)+"'"+")"
        a = a + b
        break
    else:
        b = "'"+str(i)+"'"+","

    count=count+1 
    a = a + b
    
f= open("sql-output.txt","w+")

f.write(a)
f.close()

print(type(a))
print(count)

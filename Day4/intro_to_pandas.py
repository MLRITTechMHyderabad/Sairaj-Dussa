import pandas as pd

"""d = [10, 20, 30, 40]

s = pd.Series(d)

print(s)"""


di = {
    "name": ['sairaj', 'naresh', 'Ram'],
    "city": ['wgl', 'kmm', 'vzg'],
}

#to convert into data set we use pd.DataFrame
df = pd.DataFrame(di, columns = ["name", "city"])

#to add new element into list
df["salary"] = [4, 5, 3]


#conditions to remove and fetch data
op = df[(df['city'] == "wgl") ]
print(op)

#using groupby
g = df.groupby('salary').sum()
print(g)
g = df.groupby('city').agg({'city':['count'], 'salary':['max']})
print(g)


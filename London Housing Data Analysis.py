import pandas as pd

df=pd.read_csv(r"C:\Users\Harold\Desktop\python\projects\Dataset  Project 5  London Housing Data Analysis.csv")

print(df)

print(df.count())
print(df.columns)
print(df.shape)
print(f"The null values are as follows : \n {df.isnull().sum()}")

import seaborn as sns
import matplotlib.pyplot as plt
print(f"The graph of the number of missing values in the data is \n : {sns.heatmap(df.isnull())}")
#plt.show()
df=df.fillna(0)
print(df.isnull().sum())

print("1. Convert datatype of time column to date-time format \n")

print(df.dtypes)
#Changing
df.date=pd.to_datetime(df.date)
print(df.date)
print(df.dtypes)

print("2. Add a new column 'year' in the dataframe which contains years only \n")
#df['New year']=df.date.dt.year
df.insert(3,'year',df.date.dt.year)
#This adds the New Year column after the last column in then dataset
print(df)

print("3. Add a new column 'month' and 2nd columnin the df which contains month only \n")

df.insert(2,'month',df.date.dt.month)
print(df)

print("4. Remove the columns 'year' and 'month' from the dataframe \n ")

df.drop(['month','year'],axis=1,inplace=True)
print(df)
print("5. Show all the records where 'No of crimes'are there ? \n ")

crimes=df[df.no_of_crimes == 0]
print(f"You can move into \n {crimes} and the number of such records are  {len(df[df.no_of_crimes == 0])}")
print(df['area'].value_counts())
print("What is the maximum and minimum 'no of crime' recorded per year ? \n ")
print(df)
pd.to_numeric(df.no_of_crimes)
print(df.groupby('area').no_of_crimes.max())
print(df.groupby('area').no_of_crimes.min())
print(df.groupby('area').no_of_crimes.min().sort_values(ascending=True))


print("6. Maximum and minimum 'average price' per year in england ? \n ")

df['year']=df.date.dt.year
#after adding a new column
df1= df[df.area == 'england']
print(df1)

print(f"The maximum average price per year in england is {df.groupby('year').average_price.max()}")
print(f"The minimum average price per year in england is {df.groupby('year').average_price.min()}")
print(f"The mean average price per year in england is {df.groupby('year').average_price.mean()}")


print("7. Show total count of records of each area, where average price is less than 100,000")
pd.to_numeric(df.average_price)
print(f" The total count of records of each 'area', where 'average price' is less than 100,000 are \n {df[df.average_price<100000].area.value_counts()}")

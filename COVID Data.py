import pandas as pd

covid=pd.read_csv(r"C:\Users\Harold\Desktop\python\projects\Dataset  Project 4  Covid Data Analysis.csv")
print(covid)
print(covid.shape)
print(covid.columns)
print(f"The number of values in each column is \n {covid.count()}")
print(f"The missing values are \n {covid.isnull().sum()}")

import seaborn as sns
import matplotlib.pyplot as plt
sns.heatmap(covid.isnull())
#plt.show()
print("The plot shows that only State variable has 181 missing values")

print("Q1. Show the number of confirmed, deaths and recovered cases in each region \n")


#print(covid.groupby('Region').sum()) #Soln1
#covid.drop(columns='Date',inplace=True)
#covid.drop(columns='State',inplace=True)
print(covid.groupby('Region').sum())
print(covid.columns)
print(covid.groupby('Region')[covid.columns[3:]].sum())
#covid.groupby('Region')['Confirmed'].sum().sort_values(ascending=False).head(20)


print("Q2 Remove all records where confirmed cases is less than 10 \n")

#for x in covid.index:
#    if covid.loc[x, 'Confirmed'] < 10:
#        covid.drop(x, inplace=True)

#print(covid['Confirmed'].sort_values(ascending=False))

covid=covid[~(covid.Confirmed<10)]#
#To remove the a set of vrows from a column variable, use the syntax df[~(df.Variable=conditions)]
print(covid)#All the values less than 10 are removed from he data

print("Q3. In which region were maximum number of confirmed cases recorded ?")
#since we made changes in question 2, I'll reimport the data

covid=pd.read_csv(r"C:\Users\Harold\Desktop\python\projects\Dataset  Project 4  Covid Data Analysis.csv")
max= covid.groupby('Region').Confirmed.sum().sort_values(ascending=False).head(20)
#Choose the first 20 values
print(max)
print (f"The region with the maximum number of cases was the US at 1039909 ")

print("Q4. In which region were minimun number of death cases recorded ?")

deaths=covid.groupby('Region').Deaths.sum().sort_values(ascending=True).head(40)
print(deaths)
print(f""" \n \n Least deaths were : Liechtenstein                       1
Maldives                            1
Gambia                              1
Eswatini                            1
Guinea-Bissau                       1
Equatorial Guinea                   1
Mauritania                          1
Cabo Verde                          1
Benin                               1
Burundi                             1
Suriname                            1
Brunei                              1 \n \n""")
print("Q5. How many 'confirmed, deaths and recovered' cases were reported from Kenya till 29 April 2020 ?")

kenya=covid[covid.Region == 'Kenya']
print(kenya)

print("Sort wrt no of confirmed cases in ascending order \n")
asc= covid.sort_values(by=['Confirmed'],ascending=True).head(50)
print(f"The dataframe sorted wrt the confirmed cases outputs {asc}")

print("Sort wrt no of recovered cases in descending order \n")
dsc= covid.sort_values(by=['Recovered'],ascending=False).head(50)
print(f"The dataframe sorted wrt the recovered cases outputs {dsc}")


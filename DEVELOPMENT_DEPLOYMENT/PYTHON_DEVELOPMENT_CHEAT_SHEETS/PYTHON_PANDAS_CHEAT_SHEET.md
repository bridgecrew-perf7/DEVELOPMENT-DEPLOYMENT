# Pandas Cheat Sheet
install pip numpy and pandas
```python3
sudo apt install python3-pip
pip install numpy
pip install pandas
pip install xlrd
import pandas as pd
```
csv spreadsheet to statistics
```python3
df = pd.read_CSV (r"/file.csv")

# column operations
mean1 = df["column1"].mean()
sum1 = df["column1"].sum()
max1 = df["column1"].max()
min1 = df["column1"].min()
count1 = df["column1"].count()
median1 = df["column1"].median()
std1 = df["column1"].std()
var1 = df["column1"].var()  

print(count)

# variable operations
bundle_var1_sum = df.groupby(["var1"]).sum()
bundle_var2_count = df.groupby(["var2"]).count()

print(bundle_var1_sum)
```
create dataframes
```python3
# dictionary with lists
import pandas as pd

data = {"column1":  [1, 0],
        "column2": [0, 1],
        }

df = pd.DataFrame (data, columns = ["column1","columns2"])

print(df)

# csv or excel file to df
columns1_2 = pd.read_CSV (r"/file.csv")
# columns1_2 = pd.read_excel (r"/file.xlsx")

df = pd.DataFrame(subset, columns1_2= ["column1","column2"])

print(df)
```
replace entries in columns
```python3
df["matches"] = df["first_name"].apply(lambda x: "Match" if x == "Paul" else "Mismatch")
df.loc[(df["first_name"] == "Peter") | (df["first_name"] == "Petra"), "name_match"] = "Match"  
df.loc[(df["first_name"] != "Peter") & (df["first_name"] != "Petra"), "name_match"] = "Mismatch"  
```
concat columns
```python3
concat_df = df["column1"].map(str) + df["column2"].map(str)

combined_df = pd.DataFrame(concat_df, columns=["combined"])
max1 = combined_df["combined"].max()
```
pivot tables
```python3
pivot1 = df.pivot_table(index=["Name"], values=["Income"], aggfunc="sum")
pivot2 = df.pivot_table(index=["Name"], values=["Income"], aggfunc="max")
pivot3 = df.pivot_table(index=["Name"], values=["Income"], aggfunc={"median","mean","min"}
```
plot tables
```python3
import matplotlib.pyplot as plt
pivot3 = df.pivot_table(index=["Name"], values=["Income"], aggfunc={"median","mean","min"}.plot()
plt.show()
```

## 3. Read in a CSV file ##

import pandas
food_info = pandas.read_csv("food_info.csv")
print(type(food_info))

## 4. Exploring the DataFrame ##

print(food_info.head(3))
dimensions = food_info.shape
print(dimensions)
num_rows = dimensions[0]
print(num_rows)
num_cols = dimensions[1]
print(num_cols)

first_twenty = food_info.head(20)

## 7. Selecting a row ##

hundredth_row = food_info.loc[99]
print(hundredth_row) 

## 8. Data types ##

print(food_info.dtypes)
food_info.dtypes

## 9. Selecting multiple rows ##

print("Rows 3, 4, 5 and 6")
print(food_info.loc[3:6])

print("Rows 2, 5, and 10")
two_five_ten = [2,5,10]
print(food_info.loc[two_five_ten])
last_rows = food_info.loc[food_info.shape[0]-5:food_info.shape[0]]

## 10. Selecting individual columns ##

# Series object.
ndb_col = food_info["NDB_No"]
print(ndb_col)

# Display the type of the column to confirm it's a Series object.
print(type(ndb_col))

saturated_fat = food_info["FA_Sat_(g)"]
cholesterol = food_info["Cholestrl_(mg)"]

## 11. Selecting multiple columns by name ##

zinc_copper = food_info[["Zinc_(mg)", "Copper_(mg)"]]

columns = ["Zinc_(mg)", "Copper_(mg)"]
zinc_copper = food_info[columns]

columns = ["Selenium_(mcg)","Thiamin_(mg)"]
selenium_thiamin = food_info[columns]

## 12. Practice ##

print(food_info.columns)
print(food_info.head(2))

col_name = food_info.columns
col_name = col_name.tolist()

gram_columns = []
for each in col_name:
    if each.endswith("(g)"):
        gram_columns.append(each)

gram_df = food_info[gram_columns]
gram_df.head(3)
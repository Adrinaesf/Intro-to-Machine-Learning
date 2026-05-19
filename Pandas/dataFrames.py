import pandas as pd
'''
    Data Frames: 
        - A tublar data structures with rows and columns similar to spread sheets: 
        - 2D dim

    Topics: 
        - Making dataframe(Df): pd.DataFrame(data_name)
        - indwex: pd.DataFrame(data_name, index=[])
        - accessing data : df.loc[index]
        - Adding a new column: 
            - access dataframe and add value: df[column_name] = [row_val0, ...]
        - Adding a new row: 
            - making another df
                --> pd.DataFrame(listof(dic))
                --> each dict: a single row with corresponding values
            - add it to the original one. 
                --> df = pd.concat(listof(concating values))
                ex: df = pd.concat([df, new_rows])
                where type(new_rows) = dataFrames


'''

data = {
    "Name": ["Adrina", "Patric", "Bob"], 
    "Age": [20, 35, 50]
}

df = pd.DataFrame(data, index=["first person", "second person", "third person"])

print(df)
print(df.loc["first person"])

print("_____________________________________________")
# Add a new Column: 
df["Hobby"] = ["Hiking", "Eating", "Video Games"]

print(df)
print("_____________________________________________")

# Add a new row: 
new_rows = pd.DataFrame([{"Name": "Amir", "Age": 25, "Hobby": "Cars"}, 
                        {"Name": "Winnie", "Age": 5, "Hobby": "Football"}], 
                        index=["fourth person", "fifth person"])

df = pd.concat([df, new_rows])
print(df)








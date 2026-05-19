import pandas as pd
'''
    - Opening the CSV: 
        . make a data frame for it (as they are 2d)
        . df = pd.read_csv(path_of_CSVFile)
    - printing the whole data: 
        . df.to_string()

'''



df = pd.read_csv("/Users/adrina/Intro to Machine Learning/Intro-to-Machine-Learning/Pandas/freshman_kgs.csv")
print(df.to_string())
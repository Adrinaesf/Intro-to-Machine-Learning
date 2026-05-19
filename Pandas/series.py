import pandas as pd
'''
    Series: 
        - A pandas 1-Dim labeled array that can hold any data. 
        - Similar to a single column in a spredsheet (1-Dim)

    Materials: 
        - converting lists to series and costume index: 
            --> pd.Series(arrayName, index=...)

        - accessing in a series: 
            --> seriesName.loc[index]
            --> seriesName.iloc[int_index]

        - Filtering the values in a series: 
            --> Take the series[]
            --> and then make the filter you want inside the []
            --> seriesName[condition]
        
        - Dictionaries and series: 
            --> The index of the series is same as keys in the dictionary, and
            the values are just the value in dict
            --> series.loc[index] += value (Changing teh value in a series. )
        

'''

data = [10, 20, 30]

series = pd.Series(data, index=["a", "b", "c"])
print(series)
print("_____________________________________________")

## Exaple: apartment number and their unit: 
units = [101, 102, 103, 202, 210]
apartment_series = pd.Series(units, index=["apartment one", "apartment two", "apartment three", "apartment fourth", "apartment fifth"])

print(apartment_series)
print("Getting the unit of partment 3:")
print(apartment_series.loc["apartment three"])
print("Apartments in second floor: ")
print(apartment_series[apartment_series >= 200])

print("_____________________________________________")
calories_dict = {"Day 1": 1750, "Day 2": 1300, "Day 3": 1500}

calorie_series = pd.Series(calories_dict)

print(calorie_series)

print("Calories eaten in day 2: ")
print(calorie_series.loc["Day 2"])

print("OOPS You have cheated and you had a pizza(600 cal) on day 3: add the calorie: ")

calorie_series.loc["Day 3"] += 600
print(calorie_series.loc["Day 3"])
print("Days that had more than 1500 Calories:")
print(calorie_series[calorie_series >= 1500])



import pandas as pd
df = pd.read_csv("C:\\Users\\natha\\Documents\\NursingHome2020Python\\Nursing_Home_Deficiencies_in_Utah_2020.csv")
#df["Federal_Provider_Number"] = df["Federal_Provider_Number"].astype('string')
df['Survey Date'] = pd.to_datetime(df['Survey Date'])
print(df.dtypes)
print(df['Survey Date'])
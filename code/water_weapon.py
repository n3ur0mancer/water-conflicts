import pandas as pd
import matplotlib.pyplot as plt

# Reading the CSV
data_frame = pd.read_csv('data/conflicts_and_wars_in_relation_to_water.csv', sep=',')
data_frame.Date = pd.to_numeric(data_frame.Date, errors='coerce').dropna().astype(int)

# Printing all the data in the terminal
print(data_frame[['Date', 'Headline', 'Conflict Type', 'Country', 'Region', 'Sources']])

# Years when water was most often used as a weapon since 1 AD
is_weapon = data_frame[data_frame["Conflict Type"] == "Weapon"]
#print(is_weapon[["Conflict Type", "Date", "Region"]])

#print(is_weapon['Date'].value_counts(dropna=True, ascending=True).iloc[:15])
Year_Weapon = is_weapon['Date'].value_counts(dropna=True).iloc[:15].plot(kind='bar', title="Years when water was most often used as a weapon since 1 AD")
Year_Weapon.set_ylabel('Times used as a weapon')

plt.xticks(rotation=45, ha='right', fontsize=7)


plt.show()

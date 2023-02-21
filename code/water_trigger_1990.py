import pandas as pd
import matplotlib.pyplot as plt

# Reading the CSV
data_frame = pd.read_csv('data/conflicts_and_wars_in_relation_to_water.csv', sep=',')
data_frame.Date = pd.to_numeric(data_frame.Date, errors='coerce').dropna().astype(int)

# Printing all the data in the terminal
print(data_frame[['Date', 'Headline', 'Conflict Type', 'Country', 'Region', 'Sources']])

is_trigger = data_frame[data_frame["Conflict Type"] == "Trigger"]

# Trend of water being a trigger for conflicts since 1990
is_trigger_over_1990 = is_trigger[is_trigger["Date"] > 1989]
#print(is_weapon_over_1990[['Date','Conflict Type']])
print(is_trigger_over_1990['Date'].value_counts().sort_index(ascending=True))
plot1 = is_trigger_over_1990['Date'].value_counts().sort_index(ascending=True).plot(title = "Trend of water being a trigger for conflicts since 1990",
                                                                                    ylabel="Amount of Conflicts",
                                                                                    color='#525454',
                                                                                    linewidth=0.8,
                                                                                    style='.-')

plt.xticks(rotation=45, ha='right', fontsize=7, fontname="Helvetica")
plt.grid(linestyle='dotted', color="gray")
plot1.set_facecolor('#fcfcfc')

plt.show()
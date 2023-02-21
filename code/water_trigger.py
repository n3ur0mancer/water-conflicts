import pandas as pd
import matplotlib.pyplot as plt

# Reading the CSV
data_frame = pd.read_csv('data/conflicts_and_wars_in_relation_to_water.csv', sep=',')
# Converting the string date to int
data_frame.Date = pd.to_numeric(data_frame.Date, errors='coerce').dropna().astype(int)

# Printing all the data in the terminal
print(data_frame[['Date', 'Headline', 'Conflict Type', 'Country', 'Region', 'Sources']])

# Filtering out conflicts with trigger as conflict type
is_trigger = data_frame[data_frame["Conflict Type"] == "Trigger"]
# Printing the filtered results
print(is_trigger[["Conflict Type", "Date", "Region"]])

# Counting the occurrence of trigger as conflict type by region and plotting the result
#print(is_trigger['Region'].value_counts(dropna=True, ascending=True))
Region_Trigger = is_trigger['Region'].value_counts(dropna=True, ascending=True).plot(kind='bar',
                                                                                     title = "Regions with the most conflicts caused by water since 1 AD")
# Setting the y label
Region_Trigger.set_ylabel('Amount of Conflicts')
# Adjusting the y label features
plt.subplots_adjust(bottom=0.3)
plt.xticks(rotation=45, ha='right', fontsize=7)

# Showing the plot
plt.show()
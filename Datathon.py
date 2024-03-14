import matplotlib.pyplot as plt
import pandas as pd
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()


df = pd.read_csv('C:/Users/derek/OneDrive/Documents/Coding/Datathon/Starbucks Datathon File.csv')


def plot_average_protein_2_percent_milk():
    # Remove blank space from column names
    df.columns = df.columns.str.strip()


    # Filter rows so Beverage_Prep = '2% Milk'
    milk_2_percent_df = df[df['Beverage_prep'] == '2% Milk']


    # Group by 'Beverage' and calculate the total amount of protein
    grouped_df = milk_2_percent_df.groupby('Beverage')['Protein (g)'].sum().reset_index()


    # Calculate the average of the total protein values
    average_protein = grouped_df['Protein (g)'].mean()


    # Plot bar chart
    fig, ax = plt.subplots(figsize=(16, 8))
    bars = ax.bar(grouped_df['Beverage'], grouped_df['Protein (g)'])
   
    # Labels and Titles
    ax.set_title('Total Protein').set_xlabel('Beverage')
    ax.set_ylabel('Total Protent for Beverages with 2% Milk')
    ax.annotate(f'Average Protein: {average_protein:.2f} g', xy=(0.5, 0.95), xycoords='axes fraction', ha='center', fontsize=10)


    # Rotate x-axis labels
    plt.xticks(rotation=45, ha='right')


    # Display the actual value on top of each bar
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 2), ha='center', va='bottom')
 
    # Plot that Jawn
    plt.show()


# Call the function
plot_average_protein_2_percent_milk()


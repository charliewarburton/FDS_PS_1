import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Function to load the data from the csv file
def load_data(file):
    df = pd.read_csv(file)
    return df

def tidy_data(df):
    melted_df = pd.melt(df, id_vars="Year", var_name="Country", value_name="GDP")
    return melted_df


def line_plot(df, x, y, hue, title):
    sns.lineplot(data=df, x=x, y=y, hue=hue)
    plt.title(title)
    plt.show()
    return None

def pct_change_graph(df, x, hue, title):
    df["GDP Growth"] = df.group_by("Country")["GDP"].pct_change()
    df.dropna(inplace=True)
    sns.lineplot(data=df, x=x, y=df["GDP Growth"], hue=hue)
    plt.title(title)
    plt.show()
    return None

def indexed_graph(df, x, hue, title):
    indexed_value = df.groupby('Country')["GDP"].apply(lambda x: (x / x.iloc[0]) * 100).reset_index(level=0, drop=True)
    df["Indexed GDP"] = indexed_value
    sns.lineplot(data=df, x=x, y="Indexed GDP", hue=hue)
    plt.title(title)
    plt.show()
    return None
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Function to load the data from the csv file


def load_data(file):

    df = pd.read_csv(file)
    return df


def tidy_data(df):

    melted_df = pd.melt(df, id_vars="Year", var_name="Country",
                        value_name="GDP")
    return melted_df


def line_plot(df, x, y, hue, title):

    ax = sns.lineplot(data=df, x=x, y=y, hue=hue)
    sns.move_legend(ax, "upper left", bbox_to_anchor=(1, 1))
    plt.title(title)
    plt.show()
    return None


def pct_change_graph(df, x, hue, title):

    df["GDP Growth"] = df.groupby("Country")["GDP"].pct_change()
    df.dropna(inplace=True)
    ax = sns.lineplot(data=df, x=x, y=df["GDP Growth"], hue=hue)
    sns.move_legend(ax, "upper left", bbox_to_anchor=(1, 1))
    plt.title(title)
    plt.show()
    return None


def indexed_graph(df, x, hue, title):

    indexed_value = df.groupby('Country')["GDP"].apply(lambda x: (x / x.iloc[0]) * 100).reset_index(level=0, drop=True)  # noqa: E501
    df["Indexed GDP"] = indexed_value
    sns.lineplot(data=df, x=x, y="Indexed GDP", hue=hue)
    plt.title(title)
    plt.show()
    return None

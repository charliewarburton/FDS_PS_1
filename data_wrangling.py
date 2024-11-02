# Data wrangling from Lecture 2

import pandas as pd
import numpy as np

# Create data frame

df = pd.DataFrame(
    {
        "household_id": np.random.randint(1, 10, 20),
        "age": np.random.randint(18, 99, 20),
        "income": np.random.randint(10000, 100000, 20),
        "female": np.random.randint(0, 2, 20),
    }
)

# Function for if highest earner per household is female


def highest_earner_female(df):

    def helper(group):
        highest_earner = group.loc[group['income'].idxmax()]
        return highest_earner["female"] == 1

    return df.groupby("household_id").apply(helper)


female_df = pd.DataFrame(highest_earner_female(df))

# print(female_df.head)

# function for the aggregate functions


def aggregate_funcs(df):

    aggregated_df = df.groupby("household_id").agg(
        {
            "household_id": "count",
            "age": ["min", "max", "mean"],
            "income": ["mean", "sum"],
            "female": "sum"
        }
    )

    # aggregated df will have two levels of columns, so we need to flatten it
    aggregated_df.columns = ['_'.join(col).strip()
                             for col in aggregated_df.columns.values]

    # rename the columns
    aggregated_df = aggregated_df.rename(
        columns={
            "household_id_count": "size_hh",
            "age_mean": "mean_age",
            "age_min": "min_age",
            "age_max": "max_age",
            "income_mean": "mean_income",
            "income_sum": "total_income",
            "female_sum": "nr_female"
        }
    )

    return aggregated_df


agg_df = aggregate_funcs(df)
female_df.columns = ["main_earner_female"]

merged_df = pd.merge(agg_df, female_df, left_index=True, right_index=True)

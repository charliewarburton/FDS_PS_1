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

print(female_df.head)
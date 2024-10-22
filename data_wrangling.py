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

df["size_hh"] = df.groupby("household_id")["household_id"].transform("count")
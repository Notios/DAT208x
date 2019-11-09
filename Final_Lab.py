## Final Lab - Section 1 ##
import pandas as pd
import numpy as np

#########
# Import pandas 
import pandas as pd

# Use pandas to read in recent_grads_url
recent_grads = pd.read_csv(recent_grads_url)

# Print the shape
print(recent_grads.shape)

#########
# Print .dtypes
print(recent_grads.dtypes)

# Output summary statistics
print(recent_grads.describe())

# Exclude data of type object
print(recent_grads.describe(exclude=["object"]))

#########
# Names of the columns we're searching for missing values 
columns = ['median', 'p25th', 'p75th']

# Take a look at the dtypes
print(recent_grads[columns].dtypes)

# Find how missing values are represented
print(recent_grads["median"].unique())

# Replace missing values with NaN
for column in columns:
    recent_grads.loc[recent_grads[column] == 'UN', column] = np.nan
    
#########
# Select sharewomen column
df = pd.DataFrame(recent_grads)
sw_col = df['sharewomen']

# Output first five rows
print(sw_col.head(5))

#########
# Import numpy
import numpy as np

# Use max to output maximum values
max_sw = np.max(sw_col)

# Print column max
print(max_sw)

#########
# Output the row containing the maximum percentage of women
print(recent_grads[sw_col == max_sw])

#########
# Convert to numpy array
recent_grads_np = recent_grads[["unemployed", "low_wage_jobs"]].values


# Print the type of recent_grads_np
print(type(recent_grads_np))

#########
# Calculate correlation matrix
print(np.corrcoef(recent_grads_np[:,0], recent_grads_np[:,1]))


import pandas as pd

# Data to be represented in the DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [20, 21, 19, 22, 20],
    'Grade': [88, 92, 85, 90, 95]
}

# Create a DataFrame from the data
students_df = pd.DataFrame(data)

# Display the DataFrame
print(students_df)

# access a row (i.e., integer location)
print("\nRow 0: %s" % students_df.iloc[0])

# access a column using operator [].
print("\nAges:\n", students_df["Age"])

print("mean age: ", students_df["Age"].mean())
print("stddev age: ", students_df["Age"].std())

print("mean score: ", students["Grade"].mean())


# select row for "Bob"
print("\nBob's row:", students_df.loc["Bob"])
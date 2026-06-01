# import pandas as pd

# # Create data
# data = {
#     "Name": ["Jaswanth", "Ravi", "Kiran", "Sai"],
#     "Age": [27, 25, 30, 22],
#     "Salary": [50000, 45000, 60000, 40000]
# }

# # Create DataFrame
# df = pd.DataFrame(data)

# # print("Data:")
# # print(df)

# print("\nAverage Age:")
# print(df["Age"].mean())

# # print("\nMaximum Salary:")
# # print(df["Salary"].max())

# # print("\nPeople older than 25:")
# print(df[df["Age"] > 25])



import pandas as pd

# =========================
# LOAD FILE
# =========================

df = pd.read_csv("employees.csv")

print("\n===== HEAD =====")
print(df.head())

print("\n===== TAIL =====")
print(df.tail())

print("\n===== SAMPLE =====")
print(df.sample(5))

print("\n===== SHAPE =====")
print(df.shape)

print("\n===== COLUMNS =====")
print(df.columns)

print("\n===== DATA TYPES =====")
print(df.dtypes)

print("\n===== INFO =====")
print(df.info())

print("\n===== DESCRIBE =====")
print(df.describe())

# =========================
# COLUMN ACCESS
# =========================

print("\n===== SINGLE COLUMN =====")
print(df["salary"])

print("\n===== MULTIPLE COLUMNS =====")
print(df[["name", "salary"]])

# =========================
# FILTERING
# =========================

print("\n===== AGE > 30 =====")
print(df[df["age"] > 30])

print("\n===== SALARY > 50000 =====")
print(df[df["salary"] > 50000])

print("\n===== MULTIPLE CONDITIONS =====")
print(df[(df["age"] > 30) & (df["salary"] > 50000)])

# =========================
# SORTING
# =========================

print("\n===== SORT AGE ASC =====")
print(df.sort_values("age"))

print("\n===== SORT SALARY DESC =====")
print(df.sort_values("salary", ascending=False))

# =========================
# STATISTICS
# =========================

print("\n===== MEAN =====")
print(df["salary"].mean())

print("\n===== MAX =====")
print(df["salary"].max())

print("\n===== MIN =====")
print(df["salary"].min())

print("\n===== SUM =====")
print(df["salary"].sum())

print("\n===== COUNT =====")
print(df["salary"].count())

print("\n===== MEDIAN =====")
print(df["salary"].median())

print("\n===== STD =====")
print(df["salary"].std())

# =========================
# UNIQUE
# =========================

print("\n===== UNIQUE CITY =====")
print(df["city"].unique())

print("\n===== NUMBER OF UNIQUE CITIES =====")
print(df["city"].nunique())

# =========================
# VALUE COUNTS
# =========================

print("\n===== CITY COUNTS =====")
print(df["city"].value_counts())

# =========================
# NEW COLUMN
# =========================

df["bonus"] = df["salary"] * 0.10

print("\n===== BONUS COLUMN =====")
print(df.head())

# =========================
# UPDATE VALUES
# =========================

df.loc[df["city"] == "Hyderabad", "city"] = "HYD"

print("\n===== UPDATED CITY =====")
print(df.head())

# =========================
# DROP COLUMN
# =========================

temp_df = df.drop(columns=["bonus"])

print("\n===== COLUMN REMOVED =====")
print(temp_df.head())

# =========================
# NULL VALUES
# =========================

print("\n===== NULL COUNT =====")
print(df.isnull().sum())

# Fill nulls
df = df.fillna(0)

# Remove nulls
# df = df.dropna()

# =========================
# DUPLICATES
# =========================

print("\n===== DUPLICATES =====")
print(df.duplicated().sum())

# Remove duplicates
df = df.drop_duplicates()

# =========================
# RENAME COLUMN
# =========================

renamed = df.rename(columns={"salary": "income"})

print("\n===== RENAMED =====")
print(renamed.head())

# =========================
# GROUP BY
# =========================

print("\n===== AVG SALARY BY CITY =====")
print(df.groupby("city")["salary"].mean())

print("\n===== SUM SALARY BY CITY =====")
print(df.groupby("city")["salary"].sum())

print("\n===== COUNT BY CITY =====")
print(df.groupby("city").size())

# =========================
# TOP RECORDS
# =========================

print("\n===== TOP 10 SALARY =====")
print(df.nlargest(10, "salary"))

print("\n===== LOWEST 10 SALARY =====")
print(df.nsmallest(10, "salary"))

# =========================
# APPLY FUNCTION
# =========================

df["salary_lakh"] = df["salary"].apply(
    lambda x: round(x / 100000, 2)
)

print("\n===== APPLY =====")
print(df[["salary", "salary_lakh"]].head())

# =========================
# ITERATE ROWS
# =========================

for index, row in df.head(3).iterrows():
    print(index, row["name"])

# =========================
# LOC
# =========================

print("\n===== LOC =====")
print(df.loc[0])

# =========================
# ILOC
# =========================

print("\n===== ILOC =====")
print(df.iloc[0])

# =========================
# QUERY
# =========================

print("\n===== QUERY =====")
print(df.query("age > 30"))

# =========================
# EXPORT
# =========================

df.to_csv("output.csv", index=False)

print("\n===== SAVED =====")
print("output.csv created successfully")

print("\n===== FINISHED =====")
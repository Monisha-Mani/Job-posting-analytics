# Import Required Libraries

import pandas as pd


# Load Final Engineered Dataset

df = pd.read_csv(
    "../data/cleaned/final_engineered_jobs_dataset.csv",
    low_memory=False
)

print(df.head())


# Convert Posted Date Column

df["posted_date"] = pd.to_datetime(
    df["posted_date"],
    errors="coerce"
)


# Remove Null Dates

df = df.dropna(subset=["posted_date"])


# Use Only Real-Time Portal Data

# Kaggle dataset is retained for ML training purposes.
# It is excluded from market trend analysis because it contains
# large historical/synthetic records that may distort
# real-time skill demand insights.

real_time_portals = [
    "Naukri",
    "Foundit",
    "LinkedIn",
    "Indeed"
]

df = df[df["portal_name"].isin(real_time_portals)]

print(df["portal_name"].value_counts())


# Filter Last 3 Months Data

latest_date = df["posted_date"].max()

three_months_back = latest_date - pd.DateOffset(months=3)

df_recent = df[df["posted_date"] >= three_months_back]

print(df_recent.shape)


# Create Skill Demand Dataset

skills = [
    "python_flag",
    "sql_flag",
    "power_bi_flag",
    "tableau_flag",
    "excel_flag",
    "selenium_flag"
]

skill_demand = df_recent[skills].sum().reset_index()

skill_demand.columns = ["skill", "demand_count"]

skill_demand = skill_demand.sort_values(
    by="demand_count",
    ascending=False
)

print(skill_demand)


# Analyze Skill Demand By Job Role

role_skill_analysis = df_recent.groupby(
    "standardized_role"
)[skills].sum()

print(role_skill_analysis.head())


# Find Top Skill Per Role

top_skill_per_role = role_skill_analysis.idxmax(axis=1).reset_index()

top_skill_per_role.columns = [
    "job_role",
    "top_skill"
]

print(top_skill_per_role)


# Analyze Skill Demand By Portal

portal_skill_analysis = df_recent.groupby(
    "portal_name"
)[skills].sum()

print(portal_skill_analysis)


# Analyze Monthly Skill Demand

df_recent = df_recent.copy()

df_recent["posting_month"] = df_recent[
    "posted_date"
].dt.to_period("M")

monthly_skill_trend = df_recent.groupby(
    "posting_month"
)[skills].sum()

print(monthly_skill_trend)


# Save Skill Demand Analysis Results

skill_demand.to_csv(
    "../data/cleaned/skill_demand_summary.csv",
    index=False
)

role_skill_analysis.to_csv(
    "../data/cleaned/role_skill_analysis.csv"
)

top_skill_per_role.to_csv(
    "../data/cleaned/top_skill_per_role.csv",
    index=False
)

portal_skill_analysis.to_csv(
    "../data/cleaned/portal_skill_analysis.csv"
)

monthly_skill_trend.to_csv(
    "../data/cleaned/monthly_skill_trend.csv"
)

print("Skill Demand Analysis Completed Successfully")